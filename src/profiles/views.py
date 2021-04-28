from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate, login)
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserCreateForm


@login_required
def user_profile(request):
    """Display user profile information."""
    user = request.user
    return render(request, 'profiles/profile_detail.html', {'user': user})


def sign_up(request):
    """User sign-up view."""
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )
            return HttpResponseRedirect(reverse('accounts:profile'))
    return render(request, 'profiles/sign_up.html', {'form': form})
