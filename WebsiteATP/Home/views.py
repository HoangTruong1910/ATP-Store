from django.shortcuts import render
from django.http import HttpResponse

# Trang Chủ :
def trangchu(request):
    return render(request, 'pages/trangchu.html')

def regist_login(request):
    return render(request,'pages/regist-login.html')

def products(request):
    return render(request,'pages/products.html')
