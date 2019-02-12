from django.contrib import admin

# Register your models here.
from .models import User
from .forms import MyUserChangeForm
from django.contrib.auth.admin import UserAdmin

class MyUserAdmin(UserAdmin):
	form = MyUserChangeForm

	fieldsets = UserAdmin.fieldsets + (
		(None, {'fields': ('user_type',)}),
	)

admin.site.register(User, MyUserAdmin)