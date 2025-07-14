from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_complaint, name='submit_complaint'),
    
    # User authentication and dashboard
    path('register/', views.user_register, name='user_register'),
    path('user/login/', views.user_login, name='user_login'),
    path('user/logout/', views.user_logout, name='user_logout'),
    path('user/dashboard/', views.user_dashboard, name='user_dashboard'),
    
    # Admin authentication and dashboard
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/logout/', views.admin_logout, name='admin_logout'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # Complaint management (admin only)
    path('complaint/<int:complaint_id>/resolve/', views.resolve_complaint, name='resolve_complaint'),
    path('complaint/<int:complaint_id>/edit/', views.edit_complaint, name='edit_complaint'),
    path('complaint/<int:complaint_id>/delete/', views.delete_complaint, name='delete_complaint'),
]
