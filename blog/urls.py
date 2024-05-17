from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('periodo/', views.periodo_list, name='periodo_list'),
    path('asignatura/', views.asignatura_List, name='asignatura_List'),
    path('profesor/', views.profesor_List, name='profesor_List'),
    path('estudiante/', views.estudiante_list, name='estudiante_list'),
    path('nota/', views.nota_List, name='nota_List'),
    path('detallenota/', views.detallenota_List, name='detallenota_List'),
]