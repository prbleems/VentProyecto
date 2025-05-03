"""
URL configuration for vent project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Vent Admin"
admin.site.site_title = "Panel Vent"
admin.site.index_title = "Bienvenido a Vent"

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas de login, logout, password reset, etc.
    path('accounts/', include('django.contrib.auth.urls')),

    # Tu signup y demás vistas de users
    path('accounts/', include('users.urls',    namespace='users')),

    path('',          include('catalog.urls',  namespace='catalog')),
    path('cart/',     include('cart.urls',     namespace='cart')),
    path('orders/',   include('orders.urls',   namespace='orders')),
]

# Servir archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)