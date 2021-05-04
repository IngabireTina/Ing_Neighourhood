from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from app.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app.models import *

# Create your views here.

def dashboard(request):
    hood = Hood.objects.all()
    context={
        'hood':hood,
    }
    return render(request, 'hoods.html',context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def profile(request, username):
    if request.method == 'POST':
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if prof_form.is_valid():
            prof_form.save()
            return redirect(request.path_info)
    else:
        prof_form = UpdateUserProfileForm(instance=request.user.profile)

    context = {
        'prof_form': prof_form,
         }
    return render(request, 'profile.html', context)

