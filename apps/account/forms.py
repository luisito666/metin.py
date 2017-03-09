from django import forms
from django.contrib.auth.models import User
from apps.account.models import Account
from django.db import models
from datetime import datetime   
from django.utils.translation import ugettext_lazy as _

from captcha.fields import ReCaptchaField

import re

"""
Diccionarios Espaciales con mensajes de error
"""
ERROR_MESSAGES_USER = { 
                        'required': 'el nombre de usuario es requerido',
                        'unique': 'el nombre de usuario ya esta registrado',
                        'invalid': 'ingrese un nombre de usuario valido', 
                      }

ERROR_MESSAGES_GENERAL = { 
                        'required': 'este campo es requerido',                        
                      }

ERROR_MESSAGES_PASSWORD = { 
                          'required': 'el password es requerido'
                          }

ERROR_MESSAGES_EMAIL =  {  
                          'required': 'el email es requerido',
                          'invalid': 'ingrese un correo valido',
                        }               

"""
Funciones que realizan validaciones en los formularios
"""

def valida_5(value_login):
  if re.search(r'[\s]', value_login):
    raise forms.ValidationError('El login no puede contener espacion en blanco')

def valida_6(value_login):
  if len(value_login) <= 4:
    raise forms.ValidationError('el nombre de usuario debe contener mas de 4 caracteres')

def must_be_gt(value_password):
  if len(value_password) < 5:
    raise forms.ValidationError('el password debe contener por lo menos 5 caracteres')

def valida_2(value_social_id):
  if value_social_id <= 0:
    raise forms.ValidationError('el codigo debe ser un valor positivo.')

def valida_3(value_social_id):
  if len(str(value_social_id)) <= 6:
    raise forms.ValidationError('el codigo debe tener 7 caracteres')

def valida_4(value_social_id):
  if len(str(value_social_id)) >= 8:
    raise forms.ValidationError('el codigo no puede contener mas de 7 caracteres')

#Formulario de registro principal
class CreateUserForm(forms.ModelForm):
  login = forms.CharField(max_length=30, error_messages = ERROR_MESSAGES_USER, validators = [valida_5, valida_6])
  password = forms.CharField(max_length=30, widget = forms.PasswordInput(), validators = [must_be_gt] ,error_messages = ERROR_MESSAGES_PASSWORD)
  real_name = forms.CharField(max_length=50, error_messages = ERROR_MESSAGES_GENERAL)
  email = forms.EmailField(max_length=30 , error_messages = ERROR_MESSAGES_EMAIL )
  social_id = forms.IntegerField( error_messages = ERROR_MESSAGES_GENERAL, validators = [valida_2, valida_3, valida_4])  
  capcha = ReCaptchaField()

  class Meta:
    model = Account
    fields = [
      'login',
      'password',
      'real_name',
      'email',
      'social_id',      
    ]
    labels = {
      'login': _('Nombre de Usuario'),
      'password': _('Contrasena'),
      'real_name': _('Nombre real'),
      'email': _('Correo'),
      'social_id': _('Codigo de borrado'),
    }

#Formulario que se renderiza en el login
#este formulario solo se renderiza no se realiza otras labores con el
class CustomLoginForm(forms.Form):
  login = forms.CharField(max_length=30, validators=[valida_5])
  password = forms.CharField(max_length=30, widget = forms.PasswordInput(), validators = [must_be_gt] ,error_messages = ERROR_MESSAGES_PASSWORD)
  capcha = ReCaptchaField()

  """
  class Meta:
    model = Account
    fields = [
      'login',
      'password',
    ]
    labels = {
      'login': 'Nombre de Usuario',
      'password': 'Contrasena',
    }"""

#formulario que se renderiza en el cambio de password
#este formulario solo se renderiza no se realiza otras labores con el
class CustomChangePassword(forms.ModelForm):
  password = forms.CharField(max_length=30, widget = forms.PasswordInput(), validators = [must_be_gt] ,error_messages = ERROR_MESSAGES_PASSWORD)
  new_password = forms.CharField(max_length=30, widget = forms.PasswordInput(), validators = [must_be_gt] ,error_messages = ERROR_MESSAGES_PASSWORD)
  new_password_again = forms.CharField(max_length=30, widget = forms.PasswordInput(), validators = [must_be_gt] ,error_messages = ERROR_MESSAGES_PASSWORD)

  class Meta:
    model = Account
    fields = [      
      'password',
    ]

class ResPassword(forms.Form):
  login = forms.CharField(max_length=30, validators=[valida_5])
  email = forms.CharField(max_length=30, validators = [valida_5] ,error_messages = ERROR_MESSAGES_PASSWORD)
  capcha = ReCaptchaField()
  """
  class Meta:
    model = Account
    fields = [
      'login',
      'email',
    ]
    labels = {
      'login': 'Nombre de Usuario',
      'email': 'Correo electronico',
    }"""