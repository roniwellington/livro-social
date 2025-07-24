from django.urls import path
from livros.views import index

urlpatterns = [
    path('', index)
]