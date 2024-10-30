"""
URL configuration for strona_Matek project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageAPIView.as_view(), name='home_page'),
    path('zrealizowane_projekty/', views.ProjectsDoneListAPIView.as_view(), name='projects_done'),
    path('kontakt/', views.ContactFormAPIView.as_view(), name='contact'),
    path('o_nas/', views.AboutUsAPIView.as_view(), name='about_us'),
    path('oferta/', views.ServicesAPIView.as_view(), name='services'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
