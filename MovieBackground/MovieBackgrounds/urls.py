from django.urls import path
from . import views
from .views import MovieInformations,MovieTops,MovieClassfiy,MovieHot


urlpatterns=[
    path('',views.index),
    path('api/information',MovieInformations.as_view()),
    path('api/top250',MovieTops.as_view()),
    path('api/classfiy',MovieClassfiy.as_view()),
    path('api/hot',MovieHot.as_view())
]
