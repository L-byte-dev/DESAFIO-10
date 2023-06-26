from django.urls import path
from core import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('publicaciones/', views.publicaciones_view, name='publicaciones'),
    path('contactos/', views.contactos_view, name='contactos'),
    path('registrarse/', views.registrarse_view, name='registrarse'),
    path('iniciar-sesion/', views.iniciar_sesion_view, name='iniciar-sesion'),
    path('cerrar-sesion/', views.cerrar_sesion_view, name='cerrar-sesion'),
]
