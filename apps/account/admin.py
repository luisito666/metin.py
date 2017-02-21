from django.contrib import admin

from apps.account import models

class AccountDisplay(admin.ModelAdmin):
	list_display = ('id', 'login', 'real_name', 'email', 'status', 'coins', 'a_points', 'votecoins')
	search_fields = ['login' , 'real_name']


admin.site.register(models.Account, AccountDisplay)