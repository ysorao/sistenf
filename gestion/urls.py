from django.urls import path
from . import views

urlpatterns = [
    path('/', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('dashboard/cuidadora/', views.dash_cuidadora, name='dashboard_cuidadora'),
    path('dashboard/coordinador/', views.dash_coordinador, name='dashboard_coordinador'),
    path('dashboard/admin/', views.dash_admin, name='dashboard_admin'),
    path('logout/', views.logout_view, name='logout'),
    path('cuidadora/nota/', views.registrar_nota, name='registrar_nota'),
    path('turno/<int:turno_id>/estado/<str:nuevo_estado>/', views.cambiar_estado_turno, name='cambiar_estado_turno'),
]
