from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name = 'home'),

    path('pessoas', lista_pessoas, name = 'lista_pessoas'),
    path('pessoas_create', pessoa_create, name = 'pessoa_create'),

    path('veiculos', lista_veiculos, name = 'lista_veiculos'),
    path('veiculos_create', veiculo_create, name = 'veiculo_create'),

    path('movrot', lista_movrotativo, name = 'lista_movrot'),
    path('movrot_create', movrot_create, name = 'movrot_create'),

    path('mensalista', lista_mensalista, name = 'lista_mensalista'),
    path('mensalista_create', mensalista_create, name = 'mensalista_create'),

    path('movmensalista', lista_movmensalista, name = 'lista_movmensalista'),
    path('movmensalista_create', movmensalista_create, name = 'movmensalista_create'),

]
