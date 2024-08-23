from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile

def Librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(Librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')