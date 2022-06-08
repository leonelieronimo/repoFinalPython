from django.shortcuts import render
from django.db.models import Q

from app_coder.models import Pedidos, Stock, Cliente, Envios
from app_coder.forms import PedidosForm, ClienteForm, EnviosForm


def index(request):
    return render(request, "app_coder/home.html")


def clientes(request):
    clientes = Cliente.objects.all()

    context_dict = {
        'clientes': clientes
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/clientes.html"
    )


def pedidos(request):
    pedidos = Pedidos.objects.all()

    context_dict = {
        'pedidos': pedidos
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/pedidos.html"
    )


def stock(request):
    stock = Stock.objects.all()

    context_dict = {
        'stock': stock
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/stock.html"
    )


def envios(request):
    envios = Envios.objects.all()

    context_dict = {
        'envios': envios
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/envios.html"
    )


def form_hmtl(request):

    if request.method == 'POST':
        pedido = Pedidos(name=request.POST['name'], code=request.POST['code'])
        pedido.save()

        pedidos = Pedidos.objects.all()
        context_dict = {
            'pedidos': pedidos
        }

        return render(
            request=request,
            context=context_dict,
            template_name="app_coder/pedidos.html"
        )

    return render(
        request=request,
        template_name='app_coder/formHTML.html'
    )


def pedidos_forms_django(request):
    if request.method == 'POST':
        pedido_form = PedidosForm(request.POST)
        if pedido_form.is_valid():
            data = pedido_form.cleaned_data
            pedido = Pedidos(name=data['name'],
                last_name=data['last_name'],
                telephone=data['telephone'],  
                respuesto=data['respuesto'])
            pedido.save()

            pedidos = Pedidos.objects.all()
            context_dict = {
                'pedidos': pedidos
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/pedidos.html"
            )

    pedido_form = PedidosForm(request.POST)
    context_dict = {
        'pedido_form': pedido_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/pedidos_django_forms.html'
    )


def clientes_forms_django(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            data = cliente_form.cleaned_data
            cliente = Cliente(
                name=data['name'],
                last_name=data['last_name'],
                email=data['email'],
                cuit=data['cuit'],
            )
            cliente.save()

            clientes = Cliente.objects.all()
            context_dict = {
                'clientes': clientes
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/clientes.html"
            )

    cliente_form = ClienteForm(request.POST)
    context_dict = {
        'cliente_form': cliente_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/clientes_django_forms.html'
    )


def envios_forms_django(request):
    if request.method == 'POST':
        envios_form = EnviosForm(request.POST)
        if envios_form.is_valid():
            data = envios_form.cleaned_data
            envio = Envios(
                name=data['name'],
                last_name=data['last_name'],
                city=data['city'],
                adress=data['adress'],
                telephone=data['telephone'],
                code_postal=data['code_postal'],              
                due_date=data['due_date'],
                is_delivered=data['is_delivered'],
            )
            envio.save()

            envios = Envios.objects.all()
            context_dict = {
                'envios': envios
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/envios.html"
            )

    envios_form = EnviosForm(request.POST)
    context_dict = {
        'envios_form': envios_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/envios_django_forms.html'
    )


def search(request):
    context_dict = dict()
    if request.GET['text_search']:
        search_param = request.GET['text_search']
        pedidos = Pedidos.objects.filter(last_name__contains=search_param)
        context_dict = {
            'pedidos': pedidos
        }
    elif request.GET['respuesto_search']:
        search_param = request.GET['respuesto_search']
        pedidos = Pedidos.objects.filter(respuesto__contains=search_param)
        context_dict = {
            'pedidos': pedidos
        }
    elif request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(name__contains=search_param)
        query.add(Q(respuesto__contains=search_param), Q.OR)
        pedidos = Pedidos.objects.filter(query)
        context_dict = {
            'pedidos': pedidos
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/home.html",
    )
