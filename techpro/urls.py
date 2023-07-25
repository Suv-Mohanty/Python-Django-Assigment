"""
URL configuration for techpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from techapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.statepage),
    path('state/',views.statepage,name='state'),
    path('city/',views.citypage,name='city'),
    path('branch/',views.branchpage,name='branch'),
    path('addstate/',views.stateform,name='addstate'),
    path('addcity/',views.cityform,name='addcity'),
    path('addbranch/',views.branchform,name='addbranch'),
    path('updatestate/<state_id>',views.updatestate,name='updatestate'),
    path('updatingstate/<state_id>',views.updatingstate,name='updatingstate'),
    path('updatecity/<city_id>',views.updatecity,name='updatecity'),
    path('updatebranch/<branch_id>',views.updatebranch,name='updatebranch'),
    path('deletestate/<state_id>',views.deletestate,name='deletestate'),
    path('deletecity/<city_id>',views.deletecity,name='deletecity'),
    path('deletebranch/<branch_id>',views.deletebranch,name='deletebranch'),
    path('tech/',include('techapp.urls'))
]
