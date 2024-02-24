from django.urls import path
from . import views
from .views import CustomPasswordChangeView
from django.contrib.auth import views as auth_views

app_name = 'main'

urlpatterns = [
    path('', views.session_list, name='session-list'),
    path('sessions/new/', views.session_create, name='session-create'),
    path('sessions/<int:pk>/delete/', views.session_delete, name='session-delete'),
    path('sessions/<int:pk>/details/', views.session_details, name='session-details'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login.html'), name='logout'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
]