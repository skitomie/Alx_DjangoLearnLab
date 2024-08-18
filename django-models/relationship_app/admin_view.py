from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def Admin(user):
        return user.userprofile.role == 'Admin'

@user_passes_test(Admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

