from django.shortcuts import render
from .forms import UserForm


def my_view(request):
    form = UserForm()
    return render(request, 'my_template.html', {'form': form})

