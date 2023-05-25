from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Review
from .forms import ReviewForm

class ReviewListView(LoginRequiredMixin, ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'
    login_url = '/accounts/login/'

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_create.html'
    success_url = '/'
    context_object_name = 'create'
    login_url = '/accounts/login/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
