from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
#from .models import UserProfile

def is_admin(user):
        return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

#user = User.objects.create_user(username='john', password='password')
#user_profile = UserProfile.objects.create(user=user, role='Admin')