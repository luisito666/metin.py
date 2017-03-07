from apps.account.models import Account
from apps.player.models import Player
from django.db import connections
from django.utils import timezone

"""Esta funcion es para ver cuantas cuentas tiene el server """
def total_us():
	a = Account.objects.all().count()
	return a
"""Esta funcion es para ver cuantos player hay en el server """
def total_pl():
	a = Player.objects.all().count()
	return a

"""Esta funcion es para ver cuantas personas hay online """
def last_min():
	cursor = connections['player'].cursor()
	cursor.execute("SELECT COUNT(*) as count FROM player WHERE DATE_SUB(NOW(), INTERVAL 45 MINUTE) < last_play")
	a = cursor.fetchall()
	b = a[0][0]
	return b
"""Esta funcion es para ver cuantos jugadores en promedio hay en las ultimas 24 horas """
def last_hour():
	cursor = connections['player'].cursor()
	cursor.execute("SELECT COUNT(*) as count FROM player WHERE DATE_SUB(NOW(), INTERVAL 36 HOUR) < last_play")
	a = cursor.fetchall()
	b = a[0][0]
	return b

#Esta funcion genera password aleatorios
def aleatorio(cantidad):
	#importando modulo de python
	from random import SystemRandom

	longitud = cantidad
	valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

	cryptogen = SystemRandom()
	p = ""	

	while longitud > 0:
	  p = p + cryptogen.choice(valores)
	  longitud = longitud - 1      

	retorno = p
	return retorno

"""def token_time(now, token):
	dia = (now - token).days
	if dia >= 1:
		return False
	else:
		return True"""