from django.shortcuts import render, redirect
from django.views import View
from .models import Contact, Order, WriterBid
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        # Handle writer bid form submission
        writer_first_name = request.POST.get('first_name')
        writer_middle_name = request.POST.get('middle_name')
        writer_last_name = request.POST.get('last_name')
        writer_bio = request.POST.get('bio')
        writer_education = request.POST.get('education')
        writer_documents = request.FILES.get('documents')

        writer_bid = WriterBid(
            first_name=writer_first_name,
            middle_name=writer_middle_name,
            last_name=writer_last_name,
            bio=writer_bio,
            education=writer_education,
            documents=writer_documents
        )
        writer_bid.save()

        return redirect('success_page')
    
class OrderView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        return render(request, 'order.html')

    def post(self, request):
        email = request.POST.get('email')
        order_title = request.POST.get('order_title')
        subject = request.POST.get('subject')
        deadline = request.POST.get('deadline')
        instructions = request.POST.get('instructions')
        documents = request.FILES.get('documents')
        images = request.FILES.get('images')
        folders = request.FILES.get('folders')

        order = Order(
            email=email,
            order_title=order_title,
            subject=subject,
            deadline=deadline,
            instructions=instructions,
            documents=documents,
            images=images,
            folders=folders
        )
        order.save()

        return redirect('success_page')

def success_page(request):
    return render(request, 'success.html')

class WriterBidView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        return render(request, 'writer_bid.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        bio = request.POST.get('bio')
        education = request.POST.get('education')
        documents = request.FILES.get('documents')

        writer_bid = WriterBid(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            bio=bio,
            education=education,
            documents=documents
        )
        writer_bid.save()

        return redirect('success_page')

