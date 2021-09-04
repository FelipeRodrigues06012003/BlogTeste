from django.shortcuts import redirect, render
from . models import DataRegistro, News, Post
from . forms import RegistroForm
from django.contrib import messages
from django.views.generic import DetailView, ListView
# Create your views here.


def home(request):
    context = {
        "text": "felipecfpb@gmail.com",
        "nomes": ['Felipe', ]
    }
    return render(request, "home.html", context)


def contato(request):
    context = {}
    return render(request, "contato.html", context)


def news(request):
    obj = News.objects.get(id=1)
    context = {
        "object": obj
    }
    return render(request, "news.html", context)


def news_annual(request, year):
    list = News.objects.filter(pub_date__year=year)
    context = {
        'year': year, 'arquivo_list': list
    }
    return render(request, "news_annual.html", context)


def registro(request):
    context = {
        "form": RegistroForm
    }
    return render(request, "registro.html", context)


def addUser(request):
    form = RegistroForm(request.POST)
    if form.is_valid():
        registro = DataRegistro(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email'],
            tel=form.cleaned_data['tel']
        )
        registro.save()
        messages.success(
            message='CADASTRO REALIZADO COM SUCESSO!',
            request=request)
        return redirect('add')


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
