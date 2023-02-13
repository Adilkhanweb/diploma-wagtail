from django.shortcuts import render
from .forms import CustomUserCreationForm


# Create your views here.
def test(request):
    return render(request, "test.html", {"form": CustomUserCreationForm()})
