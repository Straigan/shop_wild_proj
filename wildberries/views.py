from itertools import product
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from rest_framework import generics
from .models import Products
from .forms import RegistrationUserForm
from .serializers import ProductsSerializers

def index(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, 'wildberries/index.html', context)

def detail_product(request, id):
    product = Products.objects.get(id=id)
    context = {'product': product}
    return render(request, 'wildberries/product_detail.html', context)

class RegisterUser(CreateView):
    form_class = RegistrationUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def favorite_product(request, id):
    if request.method == "POST":
        product = Products.objects.get(id=id)
        if not product.favorite.filter(id=request.user.id).exists():
            product.favorite.add(request.user)
            product.save() 
            return render( request, 'partials/favorite_area.html', context={'product':product})
        else:
            product.favorite.remove(request.user)
            product.save() 
            return render( request, 'partials/favorite_area.html', context={'product':product})

def favorite_list(request):
    products = Products.objects.all()
    return render(request, 'wildberries/favorite_list.html', context={'products': products})

class PoductsAPIView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers