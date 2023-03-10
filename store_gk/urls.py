"""store_gk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from products import views
from store_gk.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
from users.views import auth_view, logout_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('products/', views.all_products),
    path('products/<int:id>/', views.one_product),
    path('categories/', views.all_categories),
    path('categories/<int:category_id>/', views.one_category),

    #form
    path('products/create/', views.product_create_view),
    #user
    path('users/auth/', auth_view),
    path('users/logout/', logout_view),
    path('users/register/', register_view)
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)