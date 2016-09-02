from django.http import HttpResponse
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
    flight = get_object_or_404(voo, pk=pk)
    return render(request, 'website/voo_detail.html', {'flight':flight})
<<<<<<< HEAD

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

=======
>>>>>>> f7afd6b80e081b7582306ed65188431bb5b63361
