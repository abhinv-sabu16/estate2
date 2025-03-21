"""
URL configuration for estate2 project.

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
from django.urls import path,include
from .import views
app_name='estateapp'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    path('index/',views.index,name='index'),
    path('properties/', views.properties, name='properties'),    
    path('chat/',views.chat,name='chat'),
    path('review/',views.review,name='review'),
    path('chats/', views.chat, name='chats'),
    path('signin/',views.signin,name='signin'),
    path('register/',views.register_view,name='register'),
    path('properties-detail/',views.propertydetail,name='propertydetail'),
    path('prediction/', views.prediction_view, name='prediction'),
    path("send-otp/", views.send_otp_email, name="send_otp"),
    path("verify-otp/", views.verify_otp, name="verify_otp"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("addproperty/", views.addproperty, name="addproperty"),
    path("chatbot/",views.chatbot_view,name='chatbot_view'),
    path("agentreg/",views.agentreg,name='agentreg'),

    



]
