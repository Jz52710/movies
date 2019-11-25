from django.contrib import admin
from .models import UserAdmin,MovieInformation,MovieTop
# Register your models here.

@admin.register(UserAdmin)
class User(admin.ModelAdmin):
    list_display =('id','username','password')

@admin.register(MovieInformation)
class Movies(admin.ModelAdmin):
    list_display = ('id','mname','years','score','director','mold','act','languages','img','details','official')

@admin.register(MovieTop)
class Movies(admin.ModelAdmin):
    list_display = ('id','mname','years','score','director','mold','act','img','details')
