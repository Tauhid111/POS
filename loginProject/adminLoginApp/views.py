from django.shortcuts import render
from .models import Product, Tax, Category, Branch, Role, Permission
from django.contrib.auth import logout
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from .forms import ProductForm, CategoryForm, BranchForm, CustomUserChangeForm, ExtendedUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .decorators import allowed_users
from .forms import VATSDForm, Permission_Form, RoleForm
# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('login')

def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def is_admin_or_superuser(user):
    return user.is_superuser or user.is_staff

def role_list(request):
    roles = Role.objects.all()
    return render(request, 'role_list.html', {'roles': roles})

def create_role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('role_list')
    else:
        form = RoleForm()
    return render(request, 'create_role.html', {'form':form})

def permission_list(request):
    permissions = Permission.objects.all()
    return render(request, 'permission_list.html', {'permissions': permissions})

def create_permission(request):
    if request.method == 'POST':
        form = Permission_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('permission_list')
    else:
        form = Permission_Form()
    return render(request, 'create_permission.html', {'form':form})

def update_permission(request, permission_id):
    permission = get_object_or_404(Permission, pk=permission_id)
    if request.method == 'POST':
        form = Permission_Form(request.POST, instance=permission)
        if form.is_valid():
            form.save()
            return redirect('permission_list')
    else:
        form = Permission_Form(instance=permission)
    return render(request, 'update_permission.html', {'form': form, 'permission': permission})

def delete_permission(request, permission_id):
    permission = get_object_or_404(Permission, pk=permission_id)
    if request.method == 'POST':
        permission.delete()
        return redirect('permission_list')
    return render(request, 'delete_permission.html', {'permission': permission})


def update_role(request, role_id):
    role = get_object_or_404(Role, pk=role_id)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('role_list')
    else:
        form = RoleForm(instance=role)
    return render(request, 'update_role.html', {'form': form, 'role': role})

def delete_role(request, role_id):
    role = get_object_or_404(Role, pk=role_id)
    if request.method == 'POST':
        role.delete()
        return redirect('role_list')
    return render(request, 'delete_role.html', {'role': role})

    
@login_required
#@allowed_users(allowed_roles=['admin'])
def create_user(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)

            role = form.cleaned_data['role']

            if role == 'admin':
                user.is_staff = True
            else:
                user.is_staff = False

            user.save()

            return redirect('users')  # Redirect to the user list view or any other desired page
    else:
        form = ExtendedUserCreationForm()
    return render(request, 'create_user.html', {'form': form})



def change_user(request):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)
        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            password_form.save()
            messages.success(request, 'Your profile was successfully updated.')
            return redirect('change_user')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)
    return render(request, 'change_user.html', {'user_form': user_form, 'password_form': password_form})

def add_product(request):
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')  # Redirect to the product list view or any other desired page
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form},)

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('products')

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form, 'product': product})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('users')


def add_tax(request):
    if request.method == 'POST':
        form = VATSDForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tax_view')  
    else:
        form = VATSDForm()
    return render(request, 'add_tax.html', {'form': form})

def tax_view(request):
    tax = Tax.objects.first()  
    vat = tax.vat
    sd = tax.sd

    context = {
        'vat': vat,
        'sd': sd,
        
    }

    return render(request, 'tax_view.html', context)

def edit_tax(request):
    tax = Tax.objects.first()

    if request.method == 'POST':
        form = VATSDForm(request.POST, instance=tax)
        if form.is_valid():
            form.save()
            return redirect('tax_view')
    else:
        form = VATSDForm(instance=tax)

    return render(request, 'edit_tax.html', {'form': form})

def calculate_final_price(product_id):
    product = Product.objects.get(id = product_id)
    tax = Tax.objects.first()
    vat_rate = tax.vat
    sd_rate = tax.sd

    vat_amount = product.price * vat_rate/100
    sd_amount = product.price * sd_rate/100

    final_price = product.price + vat_amount + sd_amount

    return final_price

def vat_included_price(request, product_id):
    final_price = calculate_final_price(product_id)

    context = {
        'final_price' : final_price,
    }
    return render(request, 'vat_included_price.html', context)


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def update_category(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'update_category.html', {'form': form, 'category': category})

def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'delete_category.html', {'category': category})

from django.db import models

@allowed_users(allowed_roles=['admin'])
def create_branch(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('branch_list')
    else:
        form = BranchForm()
    return render(request, 'create_branch.html', {'form': form})

def branch_list(request):
    branches = Branch.objects.all()
    return render(request, 'branch_list.html', {'branches': branches})

def update_branch(request, pk):
    branch = Branch.objects.get(pk=pk)
    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect('branch_list')
    else:
        form = BranchForm(instance=branch)
    return render(request, 'update_branch.html', {'form': form, 'branch': branch})

def delete_branch(request, pk):
    branch = Branch.objects.get(pk=pk)
    if request.method == 'POST':
        branch.delete()
        return redirect('branch_list')
    return render(request, 'delete_branch.html', {'branch': branch})