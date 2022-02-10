"""blogg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://d   ocs.djangoproject.com/en/3.1/topics/http/urls/
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
# from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
admin.site.site_header="Talha Sarwar"
admin.site.site_title="Talha Sarwar"
admin.site.index_title="Admin"
from django.views.generic import TemplateView # <--
urlpatterns = [
    # path('', TemplateView.as_view(template_name='base.html')),
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('',include('home.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('accounts/', include('allauth.urls')),
]
