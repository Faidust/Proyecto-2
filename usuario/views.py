from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def usuario(request):
    return render(request, "usuario.html")

def exit(request):
    logout(request)
    return redirect("home")