
from django.urls import path
from . import views
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('post/', views.ListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.DetailView.as_view(), name='post-detail'),
    path('post/new/', views.CreateView.as_view(), name='post-create'),
    path("post/<int:pk>/update/", views.UpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', views.DeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit-comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
]