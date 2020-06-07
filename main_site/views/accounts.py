from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib import messages

class LoginView(View):
    template_name = 'login.html'
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
    
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,
                                 password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials!")
            return redirect('login')

class RegisterView(View):
    template_name = 'register.html'
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken!')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username,
                                                password=password1,)
                user.save()
                return redirect('/login')

        else:
            messages.info(request, 'Password Not Matching!')
            return redirect('register')

            
class LogoutView(View):
    context = {}
    
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect('/')