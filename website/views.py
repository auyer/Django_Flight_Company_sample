from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404, get_list_or_404
import random
from django.utils import timezone
from .models import com_aerea, cidade, voo
from django.db.models import Q

# Create your views here.

def home(request):
    #return render(request, 'website/index.html', {})
    random_idx = random.randint(0, voo.objects.count() - 1)
    flight = voo.objects.all()[random_idx]
    return render(request, 'website/index.html', {'flight':flight})

def voo_list(request):
    flight = voo.objects.order_by('data_decolagem')
    return render(request, 'website/voo_list.html', {'flight':flight})

def voo_info(request,pk):
    flight = get_object_or_404(voo, pk=pk)
    return render(request, 'website/voo_detail.html', {'flight':flight})

def search_form(request):
    return render(request, 'website/searchTest.html')

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            flight = voo.objects.filter(id_destino_icontains=q)
            return render(request, 'website/search_results.html',
                {'flight': flight, 'query': q})
    return render(request, 'website/search_results.html', {'error': error})



def advanced_Search(request,ctf, ctt):
    flight1= get_list_or_404(voo.objects.filter(id_origem = ctf).filter(id_destino = ctt))
    flight2= get_list_or_404(voo.objects.filter(id_origem = ctt).filter(id_destino = ctf))

    return render(request, 'website/two_voo_detail.html', {'flightF':flight1, 'flightT':flight2})

def get_closest_to(self, target):
    closest_greater_qs = self.filter(dt__gt=target).order_by('dt')
    closest_less_qs    = self.filter(dt__lt=target).order_by('-dt')

    try:
        try:
            closest_greater = closest_greater_qs[0]
        except IndexError:
            return closest_less_qs[0]

        try:
            closest_less = closest_less_qs[0]
        except IndexError:
            return closest_greater_qs[0]
    except IndexError:
        raise self.model.DoesNotExist("O percurso não existe")

    if closest_greater.dt - target > target - closest_less.dt:
        return closest_less
    else:
        return closest_greater
