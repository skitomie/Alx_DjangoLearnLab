
from django.urls import path
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.ListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.DetailView.as_view(), name='post-detail'),
    path('posts/new/', views.CreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', views.UpdateView.as_view(), name='post-edit'),
    path('posts/<int:pk>/delete/', views.DeleteView.as_view(), name='post-delete'),
]