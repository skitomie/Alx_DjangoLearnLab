from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'