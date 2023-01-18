import datetime

from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.http import HttpResponse, Http404
from django.views import generic
from .models import Cadou, Cos
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.
# def index(request):
#     return HttpResponse("Hello world. You're at the polls index.")


class HomeCadou(generic.TemplateView):
    template_name = 'cadouri_de_poveste/home.html'

# API get cadou by ID
class DetaliiCadou(generic.DetailView):
    model = Cadou
    template_name = 'cadouri_de_poveste/detalii_cadou.html'

# API toate cadourile
class ListaCadou(generic.ListView):
    model = Cadou
    template_name = 'cadouri_de_poveste/lista_cadou.html'
    context_object_name = "cadouri"   # ce nume o sa aiba variabila in template

    def get_context_data(self, **kwargs): # Incarcam si cosul curent in pagina de lista cadou
        context = super(ListaCadou, self).get_context_data(**kwargs)
        try:
            context['cos'] = Cos.objects.filter(cos_inchis=False).latest('id')
        except Cos.DoesNotExist:
            context['cos'] = None
        return context


class ListaCategorieCadou(generic.ListView):
    model = Cadou
    template_name = 'cadouri_de_poveste/lista_cadou.html'
    context_object_name = "cadouri"


    def get_queryset(self):
        return Cadou.objects.filter(categorie = self.kwargs["input_type"]) # select * from Cadou WHERE type = ?
    # suprascriem functia care practic ruleaza query-ul sql asupra DB-ului pentru a returna lista de cadouri
    # filtram dupa categorie, inlocuind valoarea primita in urls.py (pre request)
    # valoarea primita se va incarca pe kwargs sub cheia definita in URL's (in cazul nostru input_type)



class AdaugaInCos(generic.View):

    def get (self, request, *args, **kwargs):
        return render(request,"cadouri_de_poveste/adauga_in_cos.html", {'cadou': Cadou.objects.get(pk=self.kwargs['cadou_id'])})

    def post(self, request, *args, **kwargs):
        try:
            cos = Cos.objects.filter(cos_inchis = False).latest("id")
        except Cos.DoesNotExist:
            cos = Cos(data = datetime.datetime.today(), pret_total = 0, numar_cadouri = 0, cos_inchis = False)
            cos.save()
        cadou_id = request.POST.get('cadou_id')
        cadou = Cadou.objects.get(pk=cadou_id)
        # cos.numar_cadouri = cos.numar_cadouri +1
        cos.numar_cadouri +=1
        cos.pret_total += cadou.pret
        cos.cadouri.add(cadou)
        cos.save()
        return redirect(reverse("lista_cadou"))


class AdaugaCadou(generic.CreateView):
    model = Cadou
    template_name = 'cadouri_de_poveste/form_cadou.html'
    fields = ['nume', 'pret', 'cod', 'categorie', 'descriere', 'poster']

class DetaliiCos(generic.DetailView):
    model = Cos
    template_name = 'cadouri_de_poveste/detalii_cos.html'

class StergeCos(generic.DeleteView):
    model = Cos
    template_name = 'cadouri_de_poveste/confirmare_stergere.html'
    success_url = reverse_lazy('lista_cadou')
    context_object_name = "obj"


class UpdateCos(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request,"cadouri_de_poveste/actualizare_cos.html", {'cos':Cos.objects.get(pk=self.kwargs['pk'])})
    # Dictionarul din interiorul functiei render {'cos':Cos.objects.get(pk=self.kwargs['pk'])} reprezinta obiectul context,
    # pe care il folosim in interiorul template-ului, de exemplu: {{cos.pret_total}}

    def post(self, request, *args, **kwargs):
        cos_id = request.POST.get('cos_id')
        cos = Cos.objects.get(pk =cos_id)
        cos.cos_inchis=True
        cos.save()
        return redirect(reverse("lista_cadou"))

def contact(request):
    return render(request, "cadouri_de_poveste/contact.html", {})

# def home(request):
#     return render(request, "cadouri_de_poveste/home.html", {})



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['parola']
        user = authenticate(request, username=username, password=password) # ne logam cu user = admin, parola = admin
        if user is not None:
            login(request, user)
            return redirect('home')
            # directionam login catre pagina home
        else:
            messages.success(request, ("Credentiale invalide. Incercati din nou"))
            return redirect('login')
        # returneaza eroare daca login este incorect

    else:
        return render(request, "cadouri_de_poveste/login.html", {})

def logout_user(request):
    logout(request)
    # messages.success(request, (""))
    return redirect('home')












