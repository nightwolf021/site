"""sell_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #post
    path('update_key', views.update_key.as_view(), name='update_key'),
    #post
    path('key_validate', views.key_isvalid.as_view(), name='key_validate'),
    #post
    path('send_error', views.make_log.as_view(), name='send_error'),
    ##get
    path('phone_validate', views.phone_validate.as_view(), name='phone_validate'),
    ##get
    path('interducer_validate', views.interducer_code_validate.as_view(), name='interducer_validate'),
    ##post
    path('save_details', views.save_details.as_view(), name='save_details'),
]
