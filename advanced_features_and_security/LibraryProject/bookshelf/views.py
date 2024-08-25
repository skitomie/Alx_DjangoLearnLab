from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import SomeModel
from django import forms
from django.http import HttpResponse
from django import User
from . forms import ExampleForm


@permission_required('bool_list.can_view', raise_exception=True)
def view_somemodel(request, pk):
    obj = get_object_or_404(SomeModel, pk=pk)
    return render(request, 'bookshelf/somemodel_detail.html', {'object': obj})

@permission_required('book_list.can_edit', raise_exception=True)
def edit_somemodel(request, pk):
    obj = get_object_or_404(SomeModel, pk=pk)
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'bookshelf/somemodel_edit.html', {'object': obj})

# Insecure way (prone to SQL injection)
#query = "SELECT * FROM users WHERE username = '%s'" % username

# Secure way using Django ORM
users = User.objects.filter(username=username)

def my_view(request):
    response = HttpResponse("Hello, world!")
    response['Content-Security-Policy'] = "default-src 'self'; script-src 'self' https://trusted.cdn.com"
    return response