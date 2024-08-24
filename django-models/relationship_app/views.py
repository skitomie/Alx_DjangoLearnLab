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
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm


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

@user_passes_test(Admin)
def Admin(request):
    return render(request, 'Admin.html')


def Librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(Librarian)
def Librarian(request):
    return render(request, 'Librarian.html')


def Member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(Member)
def Member(request):
    return render(request, 'Member.html')
"""

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})