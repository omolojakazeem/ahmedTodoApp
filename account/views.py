from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect


app_name = 'account'


def signup(request):
    template_name = 'account/register.html'
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            username = signup_form.cleaned_data.get('username')
            raw_password = signup_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('todo:homepage')
    else:
        signup_form = UserCreationForm()
        context = {
            'signup_form': signup_form
        }
        return render(request, template_name=template_name, context=context)


def user_login(request):
    template_name = 'account/login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo:homepage')
        else:
            return redirect('account:user_register')
    else:
        login_form = AuthenticationForm(request.POST)
        context = {
            'login_form': login_form
            }
    return render(request, template_name=template_name, context=context)


def user_logout(request):
    logout(request)
    return redirect('todo:homepage')
