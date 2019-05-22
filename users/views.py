from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm


def register(request):

    if request.method == 'POST':
        # Class to get passed to the template and generate HTML
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'{username}, your account has been created. \nSign in!')

            return redirect('Login')

    elif request.method == 'GET':
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):

    return render(request, 'users/profile.html')


# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
