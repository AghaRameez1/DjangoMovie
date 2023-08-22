"""djangoProject URL Configuration

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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import RedirectView
from graphene_django.views import GraphQLView

import Userauth
import djangorest
from djangoProject import settings

urlpatterns = [
                  path('', include('Userauth.urls')),
                  path('movies/', include('movies.urls')),
                  path('admin/', admin.site.urls),
                  url(r"graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
                  path('api-auth/', include('rest_framework.urls')),
                  path('api/', include('djangorest.urls')),
                  path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
