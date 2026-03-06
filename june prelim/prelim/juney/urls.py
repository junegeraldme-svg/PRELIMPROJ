from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('awareness/', views.awareness_view, name='awareness'),
    path('consultation/', views.consultation_view, name='consultation'),
    path('wellness/', views.wellness_view, name='wellness'),
    path('logout/', views.logout_view, name='logout'),
]