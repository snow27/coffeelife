from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('columbia/', views.columbia, name='columbia')
]
