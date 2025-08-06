from django.urls import path
from apps.usuarios.views import login, cadastro, logout

urlpatterns = [
   path('login', login,name='login'),
   path('cadastro', cadastro,name='cadastro'),
   path('logout', logout,name='logout'),
]


# Parei no curso Django autenticação de formulários e alertas
# 04.Validacoes