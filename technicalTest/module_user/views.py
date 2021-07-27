# Django
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Internal
from . import module_user

def signup(request):
    """ Basic signup view. Accepts POST. It validates the user form, if valid it creates the user object and authenticate it,
    if invalid it returns the form filled with errors. """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        module_user.debug(f'signup - received user form {form.data}')
        if form.is_valid():
            module_user.debug(f'signup - form valid')
            form.save()
            module_user.debug(f'signup - form saved')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            module_user.debug(f'signup - user {user} authenticated')
            return redirect('module_page:index')
    module_user.debug(f'signup - form invalid')
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})