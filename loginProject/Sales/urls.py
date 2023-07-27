from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from Sales.views import all_categories, category_products

urlpatterns = [
    path('sales-homepage/',TemplateView.as_view(template_name = 'sales_homepage.html'), name = 'sales_homepage'),
    path('all-categories/', all_categories, name = 'all_categories'),
    path('category-products/<int:category_id>/', category_products, name='category_products'),

    #path('add_order_item/<int:product_id>/', add_order_item, name='add_order_item'),
    #path('order/<int:order_id>/', order_details, name='order_details'),
    #path('order/<int:order_id>/add_product/<int:product_id>/', add_product_to_order, name='add_product_to_order'),
    #path('create_order/', create_order, name = 'create_order'),
    #path('order/', order, name= 'sales_order')

]