from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.views import View

from .util_moduls import user


class RegisterView(View):
    template_name = "pages/auth/register.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        
        #Post Actions
        response = user.register(request)
        return response if response else render(request, self.template_name)


class LogInView(View):
    template_name = "pages/auth/login.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        #Post Actions
        response = user.login_user(request)
        
        return response if response else render(request, self.template_name)