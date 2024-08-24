from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import Librarian

@user_passes_test(Librarian)
def Librarian(request):
    return render(request, 'Librarian.html')


#user = User.objects.create_user(username='john', password='password')
#user_profile = UserProfile.objects.create(user=user, role='Librarian')