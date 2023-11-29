from django.urls import path
from . import views

urlpatterns = [
    path('', views.trangchu, name='trangchu'),
    path('regist-login/', views.regist_login, name='regist_login'),
    path('products/', views.products, name='products'),

]
