

from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from adminLoginApp.views import logout_view
urlpatterns = [
    path('admin/', include('adminLoginApp.urls')),
    path('dj-admin/', admin.site.urls),
    path('sales/', include('Sales.urls')),
    
]


