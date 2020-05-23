from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserRegistrationForm, UserUpdateForm, UserProfileUpdate


def Register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'User has been created')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # pass_form = PasswordChangeForm(request.POST, instance=request.user)
        p_form = UserProfileUpdate(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            # pass_form.save()
            p_form.save()
            # update_session_auth_hash(request, user)
            messages.success(request, 'Your Profile has been Updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        # pass_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdate(instance=request.user.profile)
    context = {
        'u_form': u_form,
        # 'pass_form': pass_form,
        'p_form': p_form
    }

    return render(request, 'user/profile.html', context)
