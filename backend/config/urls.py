"""
URL configuration for MyDjangoApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.core.mail import send_mail
from django.urls import path, include
from django.conf import settings
from config.settings.base import env

from django.shortcuts import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def req(r):
    subject = 'Konu Başlığı'
    html_content = render_to_string('email_template.html', {'some_context': 'value'})  # HTML şablonunu yükle
    text_content = strip_tags(html_content)  # HTML'i düz metne çevir

    email = EmailMultiAlternatives(subject, text_content, 'your_email@gmail.com', ['recipient_email@gmail.com'])
    email.attach_alternative(html_content, "text/html")
    email.send()

    return HttpResponse('tm')


urlpatterns: [path] = [
    path('admin/' if settings.DEBUG else env('PRODUCT_ADMIN_PATH'), admin.site.urls),
    path('api/', include('api.urls'), name='api'),
    path('', req)
]
