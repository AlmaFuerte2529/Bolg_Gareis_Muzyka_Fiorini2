from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('', home),
   path('entrada/', entrada, name='entrada'),
   path('login/', login_request, name='login'),
   path('logout/', LogoutView.as_view(template_name = "logout.html"), name='logout'),
   path('registrate/', registrate, name='registrate'),
   path('agregarAvatar/', agregarAvatar, name= 'agregarAvatar'),
   path('editarPerfil/', editarPerfil, name= 'editarPerfil'),
   path('articulo/', Articulos, name= 'articulo'),  
   path('inicio/', home ,name='inicio'),
]