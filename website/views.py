from django.shortcuts import render
from django.utils import timezone
from .models import com_aerea,cidade,voo

# Create your views here.

def home(request):
    voo = voo.objects
    return render(request, 'website/index.html', {})

def voo_list(request):
    return render(request, 'website/voo_list.html', {})

def city_list(request):
    return render(request, 'website/city_list.html', {})

def com_aerea_list(request):
    return render(request, 'website/com_aerea_list.html', {})
