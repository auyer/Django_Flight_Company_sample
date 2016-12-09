from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404, get_list_or_404
import random
from django.utils import timezone
from .models import com_aerea, cidade, voo
from django.db.models import Q

# Create your views here.

def home(request):
    random_idx = random.randint(0, voo.objects.count() - 1)
    flight = voo.objects.all()[random_idx]

    random_idx = random.randint(0, voo.objects.count() - 1)
    flight2 = voo.objects.all()[random_idx]
    random_idx = random.randint(0, voo.objects.count() - 1)
    flight3 = voo.objects.all()[random_idx]
    random_idx = random.randint(0, voo.objects.count() - 1)
    flight4 = voo.objects.all()[random_idx]
    random_idx = random.randint(0, voo.objects.count() - 1)
    flight5 = voo.objects.all()[random_idx]
    city = cidade.objects.all()
    data = {
        'city':city,
        'flight':flight,
        'flight2':flight2,
        'flight3':flight3,
        'flight4':flight4,
        'flight5':flight5
    }
    return render(request, 'website/index.html', data)

def login(request):
    return render(request, 'website/cadastro.html')

def promo(request):
    return render(request, 'website/promo.html')

def voo_list(request):
    flight = voo.objects.order_by('data_decolagem')
    return render(request, 'website/voo_list.html', {'flight':flight})

def voo_info(request,pk):
    flight = get_object_or_404(voo, pk=pk)
    return render(request, 'website/voo_detail.html', {'flight':flight})

def search_form(request):
    return render(request, 'website/searchTest.html') #redirecionamento para a pagina html de busca

def search(request):
    error = False
    if 'q' in request.GET and 'f' in request.GET: #se o request receber o parametro de nome q
        q = request.GET['q']# entao a variavel q recebe o parametro supracitado
        f = request.GET['f']
        if not q or not f:#se o q estiver vazio
            error = True #erro se torna verdadeiro
        else: # se o q nao estiver vazio
            flight = (voo.objects.filter(id_destino=q).filter(id_origem=f))#a variavel flight recebe o resultado se o id_destino for igual a q
            return render(request, 'website/search_results.html' , {'flight': flight, 'query': q , 'f' : f})#no caso de nao haver um erro a pagina redireciona para o arquivo html de mostra de resultados levando consigo os parametros flight(contem o resultado) e q(entrada da pesquisa)
    return render(request, 'website/searchTest.html', {'error': error})#no caso de haver um erro redireciona a pagina atual com o parametro error que e tratado na mesma



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
        raise self.model.DoesNotExist("O percurso nao existe")

    if closest_greater.dt - target > target - closest_less.dt:
        return closest_less
    else:
        return closest_greater
