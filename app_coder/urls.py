from django.urls import path

from app_coder import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('clientes', views.clientes, name='Clientes'),
    path('pedidos', views.pedidos, name='Pedidos'),
    path('stock', views.stock, name='Stock'),
    path('envios', views.envios, name='Envios'),
    path('formHTML', views.form_hmtl),
    path('pedidos-django-forms', views.pedidos_forms_django, name='PedidosDjangoForms'),
    path('clientes-django-forms', views.clientes_forms_django, name='ClientesDjangoForms'),
    path('envios-django-forms', views.envios_forms_django, name='EnviosDjangoForms'),
    path('search', views.search, name='Search'),
]
