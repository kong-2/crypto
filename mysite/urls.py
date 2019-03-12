from django.contrib import admin
from django.urls import path, include
from crypto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('price/', views.price, name="price"),
]
