from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.views import View
from django.shortcuts import render, redirect

from users.forms import LoginForm, SignUpForm




class LoginView(View):
    def get(self, request):
        context = {
            'form': LoginForm()
        }

        return render(request, 'users/login.html', context)
    def post(self, request):

        form = LoginForm(request.POST)
        context = dict()

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                django_login(request, user)
                url = request.GET.get('next', 'index')
                return redirect(url)
            else:
                context["error"] = "Wrong username or password"

        context['form'] = form

        return render(request, 'login.html', context)

def logout(request):
    django_logout(request)

    return redirect('index')

class SignUpView(View):
    def get(self, request):
        context = {
            'form': SignUpForm()
        }

        return render(request, 'users/signup.html', context)
    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = User()
            cleaned_data = form.cleaned_data
            user.username = cleaned_data.get("username")
            user.first_name = cleaned_data.get("first_name")
            user.last_name = cleaned_data.get("last_name")
            user.email = cleaned_data.get("email")
            user.set_password(cleaned_data.get("password"))
            user.save()

            message = 'Usuario creado con éxito'
            django_login(request, user)
            url = request.GET.get('next', 'index')
            return redirect(url)
        else:
            message = "Se ha producido un error"

        context = {
            "form": form,
            "message":message
        }

        return render(request, 'users/signup.html', context)