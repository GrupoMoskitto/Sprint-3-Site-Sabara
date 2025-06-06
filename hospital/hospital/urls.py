"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from pacientes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar_paciente, name='cadastrar_paciente'),
    path('editar/<int:id>/', views.editar_paciente, name='editar_paciente'),
    path('excluir/<int:id>/', views.excluir_paciente, name='excluir_paciente'),
    path('listar/', views.listar_pacientes, name='listar_pacientes'),
    path('analise/', views.analise_dados, name='analise_dados'),
    path('sincronizar-iot/', views.sincronizar_iot, name='sincronizar_iot'),
]