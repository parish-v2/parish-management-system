from django.contrib import admin

# Register your models here.
from .models import User
from .forms import MyUserChangeForm
from django.contrib.auth.admin import UserAdmin
from sacrament.models import Baptism, Marriage, Confirmation, Invoice, InvoiceItems, ItemType, Profile, Minister, Sponsor, Schedule
class MyUserAdmin(UserAdmin):
	form = MyUserChangeForm

	fieldsets = UserAdmin.fieldsets + (
		("Custom Fields", {'fields': ('user_type',)}),
	)

admin.site.register(User, MyUserAdmin)
