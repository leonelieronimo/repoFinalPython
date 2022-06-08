from django.contrib import admin

from app_coder.models import Pedidos, Stock, Cliente, Envios

admin.site.register(Pedidos)

admin.site.register(Stock)

admin.site.register(Cliente)

admin.site.register(Envios)
