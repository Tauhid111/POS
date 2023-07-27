from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from adminLoginApp.models import Category, Product
from .models import Order, OrderItem
from .forms import OrderItemForm
from .forms import OrderItemFormSet
from django.utils import timezone

def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'all_categories.html', {'categories':categories})

def category_products(request, category_id):
    category = Category.objects.get( pk = category_id)
    products = Product.objects.filter(category = category)
    context = {
        'category':category, 
        'products':products,
        }
    return render (request, 'category_products.html', context)







    





