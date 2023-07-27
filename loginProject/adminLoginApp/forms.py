from django import forms
from .models import Product,Tax, Category, Role, Permission
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

User = get_user_model()

class RoleForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset = Permission.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required = False

    )
    all_permissions = forms.BooleanField(required = False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args ,**kwargs)
        self.fields['permissions'].queryset = Permission.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        select_all = cleaned_data.get('all_permissions')
        if select_all:
            cleaned_data['permissions'] = Permission.objects.all()
        return cleaned_data
    class Meta:
        model = Role
        fields = [
           'name', 'all_permissions', 'permissions' 
        ]
class Permission_Form(forms.ModelForm):
    class Meta:
        model = Permission
        fields = [
            'name'
        ]

    
class ExtendedUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(widget = forms.Select(attrs = {'class' : 'form-control'}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].choices = self.get_role_choices()

    def get_role_choices(self):
        return [(role.id, role.name) for role in Role.objects.all()]

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('role',)

class PermissionForm(forms.Form):
    permission = forms.ModelChoiceField(queryset = Permission.objects.all())
    allow = forms.BooleanField(required = False)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'  # Include all fields except 'last_login'
        exclude = ['last_login']

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control','rows': 3, 'cols': 40})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Product
        fields = [ 'name', 'category','description', 'price']



class VATSDForm(forms.ModelForm):
    class Meta:
        model = Tax
        fields = ('vat', 'sd')
    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

from django import forms
from .models import Branch

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('name', 'location')
