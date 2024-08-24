from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import Admin

@user_passes_test(Admin)
def Admin(request):
    return render(request, 'Admin.html')
#user = User.objects.create_user(username='john', password='password')
#user_profile = UserProfile.objects.create(user=user, role='Admin')