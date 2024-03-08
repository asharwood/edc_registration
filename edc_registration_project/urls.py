"""edc_registration_project URL Configuration

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
from django.urls import path, re_path, include
from register.views import register_user, select_dataset, thanks

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', select_dataset),
    re_path(r'^register/user/(?P<datasetid>\d+)', register_user),

    path('register/thanks/', thanks),

    # Uncomment the admin/doc line below to enable admin documentation:
#    path('admin/doc/',  django.contrib.admindocs.urls),


    path('captcha/', include('captcha.urls')),


]
