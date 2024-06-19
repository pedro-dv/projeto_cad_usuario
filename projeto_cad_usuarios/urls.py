
from django.urls import path
from app_cad_usuarios import views # adicionei


# home é uma função que sera criado no app 'views.py'

urlpatterns = [
    #usuarios.com
    path('', views.home, name='home'),
    #usuarios.com/usuarios
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('delete_usuario/<int:id_usuario>/', views.delete_usuario, name='delete_usuario'),
]
