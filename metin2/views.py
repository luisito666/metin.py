from django.shortcuts import render, redirect
from apps.account.funciones import *


def index(request):	
	context = {'player': total_pl(), 'account': total_us(), 'online': last_hour(), 'actualmente': last_min()}
	return render(request, 'index.html', context)

def donaciones(request):
	context = {'player': total_pl(), 'account': total_us(), 'online': last_hour(), 'actualmente': last_min()}
	return render(request, 'donaciones.html', context)
	