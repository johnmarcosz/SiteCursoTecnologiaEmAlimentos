from django.urls import path

from . import views

app_name = "contas"
urlpatterns = [
    path('cadastrarUsuario/', views.CadastrarUsuario.as_view(), name='cadastrarUsuario'),
]
