from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, UpdateProfileForm
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error


def register(request):

    if request.method == 'POST':
        # Class to get passed to the template and generate HTML
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(
                request, f'{user}, your account has been created. \nSign in!')

            return redirect('Login')

    elif request.method == 'GET':
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        #                          pass expected model to ModelForm
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your porfile has been update!')
            redirect('Profile')
    else:
        #                           pass expected model to ModelForm
        u_form = UserUpdateForm(instance=request.user)
        p_form = UpdateProfileForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
