"""blockchain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from blockchain import view


urlpatterns = [
    path('requests/', view.requests, name='requests'),
    path('upload/', view.upload, name='upload'),
    path('data_center/', view.data_center, name="data_center"),
    path('study/<str:id>', view.study, name="study"),
    path('homepage/', view.homepage, name="homepage"),
    path('', view.index, name="home"),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('uploadedstudydetails/<str:study_id>', view.uploaded_study_detail, name="uploaded_study_detail"),
]