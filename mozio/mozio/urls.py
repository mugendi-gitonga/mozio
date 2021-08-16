"""mozio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from core.views import dashboard_view, provider_view, polygon_view, delete_polygon_view, get_provider


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_view, name='dashboard-view'),
    
    path('api/v1/', include('api.urls')),

    path('dashboard/', dashboard_view, name='dashboard-view'),
    path('provider/<str:provider_id>/', provider_view, name='provider-view'),
    path('available_providers/', get_provider, name='get-provider'),
    path('provider/<str:provider_id>/<str:polygon_id>/', polygon_view, name='polygon-view'),
    path('provider/delete/<str:provider_id>/<str:polygon_id>/', delete_polygon_view, name='delete-polygon-view'),



]
