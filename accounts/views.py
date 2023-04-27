from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .forms import RegisterForm, LoginForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 == password2:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists")
                    return redirect('/accounts/register')
                elif User.objects.filter(username=username).exists():
                    messages.error(request, "Username already exists")
                    return redirect('/accounts/register')
                else:
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password1
                    )
                    user.save()
                    return redirect('/accounts/login')
            else:
                messages.error(request, 'Passwords are not equal!')
                return redirect('/accounts/register')
    else:
        form = RegisterForm()
    return render(request, "register.html", {'register_form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            print('Username or password not found')
            return redirect('/accounts/login')

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')