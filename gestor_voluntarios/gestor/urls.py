from django.urls import path
from . import views

app_name = 'voluntarios'

urlpatterns = [
    # Voluntarios
    path('voluntario/', views.voluntario_lista, name='voluntario_lista'),
    path('voluntario/crear/', views.voluntario_crear, name='voluntario_crear'),
    path('voluntario/<int:id>/', views.voluntario_detalle, name='voluntario_detalle'),
    path('voluntario/<int:id>/editar/', views.voluntario_editar, name='voluntario_editar'),
    path('voluntario/<int:id>/eliminar/', views.voluntario_eliminar, name='voluntario_eliminar'),
    
    # Eventos (similar estructura)
    path('eventos/', views.evento_lista, name='evento_lista'),
    path('evento/crear/', views.evento_crear, name='evento_crear'),
    path('evento/<int:id>/', views.evento_detalle, name='evento_detalle'),
    path('evento/<int:id>/editar/', views.evento_editar, name='evento_editar'),
    path('evento/<int:id>/eliminar/', views.evento_eliminar, name='evento_eliminar'),
]