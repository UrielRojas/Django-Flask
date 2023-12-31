"""
URL configuration for aprendiendoDjando project.

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
from django.urls import path
from django.conf import settings 
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola-mundo/', views.hola_mundo, name="hola_mundo"),
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    path('pagina-pruebas/', views.pagina, name="pagina-pruebas"),
    path('pagina-pruebas/<int:redirigir>', views.pagina, name="pagina-pruebas"),
    path('contacto/', views.contacto, name="contacto"),
    path('contacto/<str:nombre>', views.contacto, name="contacto"),
    path('contacto/<str:nombre>/<str:apellidos>', views.contacto, name="contacto"),
    path('crear-articulo/<str:title>/<str:content>/<str:public>', views.crear_articulo, name="crear_articulo"),
    path('articulo/', views.articulo, name="articulo"),
    path('editar-articulo/<int:id>', views.editarArticulo, name="editar-articulo"),
    path('articulos/', views.articulos, name="articulos"),
    path('borrar-articulo/<int:id>', views.borrarArticulo, name="borrar-articulo"),
    path('save-article/', views.saveArticle, name="save-article"),
    path('create-article/', views.createArticle, name="create-article"),
    path("create-full-article/", views.create_full_article , name="create_full_article")




]

#Configuración para cargar imágenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    #Título del panel ADMIN
admin.site.site_header = "URIEL ADMIN"
admin.site.site_title = "URIEL - ADMIN"
admin.site.index_title = "Panel de Gestión"
