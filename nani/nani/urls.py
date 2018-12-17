"""nani URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView
from hydapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.openHomePage),
    path('openHomePage/', views.openHomePage),


   # path('openServices/',views.openServices),


    path('openUser/',views.openUser),
    path('loginUser/',views.loginUser),
    path('openSignUpPage/',views.openSignUpPage),
    path('registerUser/',views.registerUser),
    path('openServicesPage/',views.openServicesPage),

    path('openContact/',views.openContact),
    path('ContactPage/',views.ContactPage),


    path('openUserHomePage/',views.openUserHomePage),
    path('openBookingPage/',views.openBookingPage),
    path('oopenbookingPage/',views.oopenbookingPage),
#    path('openPayment/',views.openPayment),
  #  path('paymentpage/',views.paymentpage),
    path('opendisplay/', views.opendisplay),
   # path('display/',views.display),

    path('openCancelPage/',views.openCancelPage),
    path('CancelPage/',views.CancelPage),
]