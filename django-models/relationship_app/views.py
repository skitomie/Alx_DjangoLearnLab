from admin_view import Admin
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile
from .models import Admin
from .models import Librarian
from .models import Member


def list_books(request):
    book = Book.objects.all()
    context = {'list_books': book}

    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def register(request):
    form = UserCreationForm()  # Use UserCreationForm() if you don't have a custom form
    return render(request, 'relationship_app/register.html', {'form': form})

#user = User.objects.create_user(username='john', password='password')
#user_profile = UserProfile.objects.create(user=user, role='ROLE_CHOICES')
"""
def Admin(user):
        return user.userprofile.role == 'Admin'
"""

@user_passes_test(Admin)
def Admin(request):
    return render(request, 'Admin.html')

"""
def Librarian(user):
    return user.userprofile.role == 'Librarian'
"""
@user_passes_test(Librarian)
def Librarian(request):
    return render(request, 'Librarian.html')

"""
def Member(user):
    return user.userprofile.role == 'Member'
"""

@user_passes_test(Member)
def Member(request):
    return render(request, 'Member.html')
