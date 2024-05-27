from django.shortcuts import render
from django.views import View
from service.models import Services

class HomeView(View):
    template_name = "index.html"
    
    def get_context_data(self):
        context = {
            "services" : Services.objects.all()
        }
        return context
    
    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    def post(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)