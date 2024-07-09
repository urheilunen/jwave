from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
	model = CustomUser
	# Если у вас есть дополнительные поля, добавьте их в fieldsets
	fieldsets = UserAdmin.fieldsets + (
	    (None, {'fields': ('birth_date', 'gender', 'city', 'relationship_status', 'subscribants')}),
	)

admin.site.register(CustomUser, CustomUserAdmin)