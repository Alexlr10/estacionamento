from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name = 'home'),

    path('pessoas', lista_pessoas, name = 'lista_pessoas'),
    path('pessoa_create', pessoa_create, name = 'pessoa_create'),
    path('pessoa_update/<int:id>/', pessoa_update, name = 'pessoa_update'),

    path('veiculos', lista_veiculos, name = 'lista_veiculos'),
    path('veiculos_create', veiculo_create, name = 'veiculo_create'),
    path('veiculo_update/<int:id>/', veiculo_update, name = 'veiculo_update'),


    path('movrot', lista_movrotativo, name = 'lista_movrot'),
    path('movrot_create', movrot_create, name = 'movrot_create'),
    path('movrot_update/<int:id>/', movrot_update, name='movrot_update'),

    path('mensalista', lista_mensalista, name = 'lista_mensalista'),
    path('mensalista_create', mensalista_create, name = 'mensalista_create'),
    path('mensalista_update/<int:id>/', mensalista_update, name='mensalista_update'),

    path('movmensalista', lista_movmensalista, name = 'lista_movmensalista'),
    path('movmensalista_create', movmensalista_create, name = 'movmensalista_create'),
    path('movmensalista_update/<int:id>/', movmensalista_update, name='movmensalista_update'),

]
