from django.shortcuts import render , get_object_or_404
from django.utils import timezone
from .models import com_aerea, cidade, voo

# Create your views here.

def home(request):
    #return render(request, 'website/index.html', {})
    flight = voo.objects.order_by('data_decolagem')
    return render(request, 'website/index.html', {'flight':flight})

def voo_list(request):
    flight = voo.objects.order_by('data_decolagem')
    return render(request, 'website/voo_list.html', {'flight':flight})

def voo_info(request,pk):
    voo = get_object_or_404(voo, pk=pk)
    return render(request, 'website/voo_detail.html', {'voo':voo})

def city_list(request):
    return render(request, 'website/city_list.html', {})

def com_aerea_list(request):
    return render(request, 'website/com_aerea_list.html', {})
