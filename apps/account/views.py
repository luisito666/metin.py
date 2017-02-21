from django.shortcuts import render, redirect
from apps.account.models import Account
from apps.account.forms import CreateUserForm
from apps.account.forms import CustomLoginForm
from apps.account.forms import CustomChangePassword
from apps.varios.models import Descarga
from apps.player.models import Guild
from apps.varios.models import Top

from apps.account.funciones import *
from django.core.mail import send_mail

from django.views.generic import CreateView, DetailView, ListView
from django.http import HttpResponseRedirect , HttpResponse
from django.core.urlresolvers import reverse_lazy

from django.db.models import Q


class Create(CreateView):
  success_url = reverse_lazy('account:exito')
  template_name = 'account/registro.html'
  model = Account 
  form_class = CreateUserForm
  def form_valid(self,form):
    self.object = form.save(commit=False)
    new_password = self.object.micryp( self.object.password )	
    self.object.password = new_password 
    self.object.save()
    return HttpResponseRedirect( self.get_success_url() )
  def get_context_data(self, **kwargs):
        context = super(Create, self).get_context_data(**kwargs)
        context['player'] = total_pl()
        context['account'] = total_us()
        context['online'] = last_hour()
        context['actualmente'] = last_min()
        return context

def login(request):
  form = CustomLoginForm()
  if request.session.has_key('id'):
    a = Account.objects.get(id=request.session['id'])
    b = Top.objects.filter(account_id=a.id)
    return render(request, 'account/logon.html',{	'session': a ,     												
    												'personajes': b,
    												'player': total_pl(),
    												'account': total_us(),
    												'online': last_hour(), 
    												'actualmente': last_min(),
    											})
  else: 
    if request.method == 'POST':  #Validando que los datos vengan por post
      if request.POST['login'] and request.POST['password']:       
        try:
          a = Account.objects.get(login=request.POST['login'])  #obteniendo datos de usuario
        except Account.DoesNotExist:          
          context = {'key':'El nombre de usuario no existe',}
          return render(request, 'account/login.html', {'context': context, 'form': form})
      else:        
        context = {'key':'Por favor no deje campos en blanco',}
        return render(request, 'account/login.html', {'context': context, 'form': form})
      b = a.micryp(request.POST['password']) #uso implicito de cursor   
      if a.password == b:
        request.session['id'] = a.id   
      if request.session.has_key('id'):
        b = Top.objects.filter(account_id=a.id)
        return render(request, 'account/logon.html', {
        												'session': a , 
        												'personajes': b,
        												'player': total_pl(), 
        												'account': total_us(), 
        												'online': last_hour(), 
        												'actualmente': last_min(), 
        											 })
      else:        
        context = {'key':'Nombre de usuario o password incorrecto',}
        return render(request, 'account/login.html', {'context': context, 'form': form})      
    else:      
      return render(request,'account/login.html', {'form': form, })

def logout(request):
  try:
    a = Account.objects.get(id=request.session['id'])    
    del request.session['id']
  except:
    pass
  return render(request, 'account/salir.html', {'datos': a} )

def changepasswd(request):
  if request.session.has_key('id'):    
    a = Account.objects.get(id=request.session['id'])
    if request.method == 'POST':
    	form = CustomChangePassword(request.POST)
    	if request.POST['new_password'] == request.POST['new_password_again']:
    		if a.password == a.micryp(request.POST['password']):
    			if form.is_valid():
    				#post = form.save(commit=False)
    				new_password = a.micryp( request.POST['new_password'] )
    				a.password = new_password
    				a.save()
    				context = { 'key':'pass existo', }
    				return render(request, 'account/password.html', {'context': context ,'form': CustomChangePassword() } )
    		else:
    			context = { 'key':'Contrasea erronea' }
    			return render(request, 'account/password.html', {'context': context ,'form': CustomChangePassword() } )
    	else:
    		#'contraseas no coinciden'
    		context = { 'key':'las nuevas contraseas no coinciden' }
    		return render(request, 'account/password.html', {'context': context ,'form': CustomChangePassword() } )
    else:
    	form = CustomChangePassword()
    	return render(request, 'account/password.html' , {'form': form})

  else:
  	return redirect('account:login')

#Funciones basicas..

def exito(request):
  context = {}
  return render(request, 'account/exito.html', context)

def descarga(request):
  a = Descarga.objects.all()
  context = { 
              'descarga': a ,
              'player': total_pl(), 
              'account': total_us(), 
              'online': last_hour(), 
              'actualmente': last_min(),
            }
  return render(request, 'account/download.html', context)

"""def top100(request):
  a = Player.objects.all().exclude(Q(name__contains='[')).order_by('-level','-exp')#[:10]
  context = { 'player': a}
  return render(request,'account/top100.html', context)
"""
class top(ListView):
  model = Top
  template_name = 'account/top100.html'
  #context_object_name = 'player'
  queryset = Top.objects.all().exclude(Q(name__contains='[')).order_by('-level','-exp')
  #queryset = Player.objects.filter(string__contains='[%]%')
  paginate_by = 20

  def get_context_data(self, **kwargs):
        context = super(top, self).get_context_data(**kwargs)
        context['player'] = total_pl()
        context['account'] = total_us()
        context['online'] = last_hour()
        context['actualmente'] = last_min()
        return context
  
class top_g(ListView):
  model = Guild
  template_name = 'account/top_g.html'
  queryset = Guild.objects.all().order_by('-level','-exp','-win', '-ladder_point')
  paginate_by = 20

  def get_context_data(self, **kwargs):
        context = super(top_g, self).get_context_data(**kwargs)
        context['player'] = total_pl()
        context['account'] = total_us()
        context['online'] = last_hour()
        context['actualmente'] = last_min()
        return context

def recuperar_password(request):
  #validando los datos que se envian por post
    if request.method == 'POST':
      a = request.POST['login']
      b = request.POST['email']
      try:
        usuario = Account.objects.get(login=a)
      except Account.DoesNotExist:
        context = {'key': 'No se encuentran registros en nuestra base de datos'}
        return render(request, 'account/rescue.html', context)

      if usuario.email == b:
        key = aleatorio(20)
        usuario.address = key
        usuario.save()
        mensaje ='Hola %s' % usuario.real_name
        mensaje+='has solicitado un email para recuperar el password'
        mensaje+='para proceder usa el siguiente <a href="https://www1.metin2kai.co/password/%s">link</a>' % key
        mensaje+='si no has solicitado el dicho cambio ignorar este correo'
        mensaje+='att: staff metin2kai.'
        """send_mail(
          'recuperacion de password',
          mensaje, 
          'soporte@metin2kai.co',
          [usuario.email],
          fail_silently=False,
          )"""
        from django.core.mail import EmailMessage
        EmailMessage(
          'Recuperar password',
          mensaje,
          to = [usuario.email],
          )

        context = {'key': 'se ha enviado un correo electronico con las instrucciones para recupear el password'}
        return render(request, 'account/rescue.html', context)
    else:
      context = {'key': 'estoy aca?'}
      return render(request, 'account/rescue.html', context)




