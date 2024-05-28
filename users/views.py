from django.shortcuts import render, redirect

from django.views import View

from .util_moduls import user
from .models import DoctorsOrUsers


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


class ProfileView(View):
    template_name = "profile.html"
    
    def get_context_data(self):
        context = {
            "user" : DoctorsOrUsers.objects.get(id= self.request.user.id )
        }    
        return context
    
    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name,context)
    
    def post(self, request):
        context = self.get_context_data()
        return render(request, self.template_name,context)