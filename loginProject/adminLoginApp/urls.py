from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from adminLoginApp.views import logout_view,users, create_user, change_user, add_product,products, delete_product, edit_product,delete_user,add_tax
from adminLoginApp.views import tax_view, edit_tax, vat_included_price, create_category, category_list, update_category
from adminLoginApp.views import delete_category, create_branch, branch_list, update_branch, delete_branch
from adminLoginApp.views import role_list, update_role, create_role, delete_role, create_permission, permission_list
from adminLoginApp.views import update_permission, delete_permission

urlpatterns=[
    path('',TemplateView.as_view(template_name = 'home.html'), name = 'home'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('logout/', logout_view, name='logout'),
    path('adminLoginApp/',users, name = 'users'),
    path('create-user/', create_user, name='create_user'),
    path('change-user/', change_user, name='change_user'),
    path('add-product/', add_product, name='add_product'),
    path('products/', products, name='products'),
    path('products/delete/<int:product_id>/', delete_product, name='delete_product'),
    path('products/edit/<int:product_id>/', edit_product, name='edit_product'),
    path('users/delete/<int:user_id>/', delete_user, name='delete_user'),
    path('add-tax/', add_tax, name='add_tax'),
    path('tax-view/', tax_view, name = 'tax_view'),
    path('tax/edit/', edit_tax, name='edit_tax'),
    path('vat_included_price/<int:product_id>', vat_included_price, name = 'vat_included_price'),
    path('category/create/', create_category, name='create_category'),
    path('category/list/', category_list, name='category_list'),
    path('category/update/<int:pk>/', update_category, name='update_category'),
    path('category/delete/<int:pk>/', delete_category, name='delete_category'),
    path('branch/create/', create_branch, name='create_branch'),
    path('branch/list/', branch_list, name='branch_list'),
    path('branch/update/<int:pk>/', update_branch, name='update_branch'),
    path('branch/delete/<int:pk>/', delete_branch, name='delete_branch'),
    #path('users/manage-permissions/<int:user_id>', manage_permissions, name='manage_permissions'),
    path('roles/', role_list, name='role_list'),
    path('roles/create/', create_role, name='create_role'),
    path('roles/<int:role_id>/update/', update_role, name='update_role'),
    path('roles/<int:role_id>/delete/', delete_role, name='delete_role'),
    path('permissions/create/', create_permission, name='create_permission'),
    path('permissions/list/', permission_list , name = 'permission_list'),
    path('permissions/<int:permission_id>/update/', update_permission, name = 'update_permission'),
    path('permissions/<int:permission_id>/delete/', delete_permission, name = 'delete_permission'),
    #path('dashboard/', TemplateView.as_view(template_name='index.html'), name = 'index'),
]