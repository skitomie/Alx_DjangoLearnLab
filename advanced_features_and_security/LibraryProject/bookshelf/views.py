from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import SomeModel

@permission_required('bookshelf.can_view', raise_exception=True)
def view_somemodel(request, pk):
    obj = get_object_or_404(SomeModel, pk=pk)
    return render(request, 'bookshelf/somemodel_detail.html', {'object': obj})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_somemodel(request, pk):
    obj = get_object_or_404(SomeModel, pk=pk)
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'bookshelf/somemodel_edit.html', {'object': obj})