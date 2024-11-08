from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
     list_display = ('username', 'email')

     fieldsets = (
         ('Credentials', {'fields':('email', 'password')}),
         ('Permission', {'fields':('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
         ('Important Dates', {'fields':('last_login', )})
         )