"""
URL configuration for MysoreHeritage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing_page,name='homepage'),
    
    path('heritage_list/', views.heritage_list, name='heritage_list'), 

    path('add_heritage', views.add_heritage,name='add_heritage'),
    path('update_heritage', views.update_heritage,name='update_heritage'),
    path('delete_heritage', views.delete_heritage,name='delete_heritage'),
    path('fetch_heritage', views.fetch_heritage,name='delete_heritage'),
    path('heritage/<int:pk>/', views.heritage_detail, name='heritage_detail'),
    path('heritage/category/<str:category_name>/', views.category_filter, name='category_filter'),


    path('add_category', views.add_category,name='add_category'),
    path('update_category', views.update_category,name='update_category'),
    path('delete_category', views.delete_category,name='delete_category'),
    path('fetch_category', views.fetch_category,name='categories'),

    path('add_location', views.add_location,name='add_location'),
    path('update_location', views.update_location,name='update_location'),
    path('delete_location', views.delete_location,name='delete_location'),
    path('fetch_location', views.fetch_location,name='delete_location'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
