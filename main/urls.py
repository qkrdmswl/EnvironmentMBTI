from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('form/', views.form, name ="form"),
    path('result/', views.result, name ="result"),
    path('loading/', views.loading),

]

