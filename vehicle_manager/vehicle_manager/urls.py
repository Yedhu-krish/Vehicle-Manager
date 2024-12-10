"""
URL configuration for vehicle_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from vehicle import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicle/add/',views.VehicleCreateVIew.as_view(),name='vehicleadd'),
    path('vehicle/view/',views.VehicleView.as_view(),name='viewvehicle'),
    path('vehicle/<int:pk>/detail',views.VehicleDetailView.as_view(),name='vehicledetailview'),
    path('vehicle/<int:pk>/delete/',views.vehicleDeleteView.as_view(),name='vehicledelete'),
    path('vehicle/<int:pk>/update',views.VehicleUpdateView.as_view(),name='vehicleupdate'),
    path('register/',views.SignUpView.as_view(),name='register'),
    path('login/',views.SignInView.as_view(),name='signin'),
    path('logout',views.LogoutView.as_view(),name='logout'),
]
