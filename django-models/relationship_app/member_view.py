from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile

def Member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(Member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

user = User.objects.create_user(username='john', password='password')
user_profile = UserProfile.objects.create(user=user, role='Member')