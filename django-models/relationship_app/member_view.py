#from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
#from .models import UserProfile

def Member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(Member)
def Member(request):
    return render(request, 'Member.html')

#user = User.objects.create_user(username='john', password='password')
#user_profile = UserProfile.objects.create(user=user, role='Member')