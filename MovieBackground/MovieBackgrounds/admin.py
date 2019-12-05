from django.contrib import admin
from .models import UserAdmin,MovieInformation,MovieTop,MovieCollection
# Register your models here.
admin.site.site_title="爱电影后台"
admin.site.site_header="爱电影后台管理"
admin.site.index_title="欢迎登陆"

@admin.register(UserAdmin)
class User(admin.ModelAdmin):
    list_display =('id','username','password')

@admin.register(MovieInformation)
class Movies(admin.ModelAdmin):
    list_display = ('id','mname','years','score','director','mold','act','languages','img','details','official')

@admin.register(MovieTop)
class Movies(admin.ModelAdmin):
    list_display = ('id','mname','years','score','director','mold','act','img','details')

@admin.register(MovieCollection)
class MovieColl(admin.ModelAdmin):
    list_display = ('id','uid','mid')
