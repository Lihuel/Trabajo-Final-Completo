from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from . import models
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


def index(request):
    return render(request, "noticias/index.html")


class NoticiasCreate(CreateView):
    model = models.Noticias
    form_class = forms.NoticiasForm
    success_url = reverse_lazy("noticias:index")


class  NoticiasList(ListView):
    model = models.Noticias

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Noticias.objects.filter(titulo__icontains=query)
        else:
            object_list = models.Noticias.objects.all()
        return object_list


class  NoticiasDetail(DetailView):
    model = models.Noticias


class  NoticiasDelete(DeleteView):
    model = models.Noticias
    success_url = reverse_lazy("noticias:noticias_list")


class  NoticiasUpdate(UpdateView):
    model = models.Noticias
    success_url = reverse_lazy("noticias:noticias_list")
    form_class = forms.NoticiasForm
