"""projeto_trainee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from API.resources import *
from API.urls import *

users_resource = UsuarioResource()
gastos_resource = GastosResource()
account_resource = ContaResource()


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    path('api/users/', include(users_resource.urls)),
    path('api/banks/', include(account_resource.urls)),
    path('api/expenses/', include(gastos_resource.urls)),
    path('', include('API.urls',namespace=''))
]