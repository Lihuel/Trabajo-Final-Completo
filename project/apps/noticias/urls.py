from django.urls import path
from . import views
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path("",views.index, name ="index"),
    path("noticias/detail/<int:pk>", views.NoticiasDetail.as_view(), name="noticias_detail"),
    path("noticias/list/", views.NoticiasList.as_view(), name="noticias_list"),
    path("noticias/create/",(views.NoticiasCreate.as_view()), name="noticias_create"),
    path("noticias/delete/<int:pk>", staff_member_required(views.NoticiasDelete.as_view()), name="noticias_delete"),
    path("noticias/update/<int:pk>", staff_member_required(views.NoticiasUpdate.as_view()), name="noticias_update"),
]