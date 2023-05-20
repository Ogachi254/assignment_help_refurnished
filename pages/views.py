from django.shortcuts import render, redirect
from django.views import View
from .models import Contact
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class contact_view(TemplateView):
    template_name = 'contact.html'

class ContactView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'  # Specify the login URL

    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        # Redirect the user to the success page
        return redirect('success_page')

def success_page(request):
    return render(request, 'success.html')
