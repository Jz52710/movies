from django.urls import path
from . import views
from .views import MovieInformations,MovieTops,MovieClassfiy,MovieHot,Logon,Login,MovieSess,MovieSearch,MovieColls


urlpatterns=[
    path('',views.index),
    path('api/information',MovieInformations.as_view()),
    path('api/top250',MovieTops.as_view()),
    path('api/classfiy',MovieClassfiy.as_view()),
    path('api/hot',MovieHot.as_view()),
    path('api/logon',Logon.as_view()),
    path('api/login',Login.as_view()),
    path('api/sess',MovieSess.as_view()),
    path('api/search',MovieSearch.as_view()),
    path('api/collection',MovieColls.as_view()),
]
