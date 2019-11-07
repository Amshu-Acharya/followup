from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from enquiry.models import Course


class IndexView(ListView):
    template_name = 'academics/index.html'
    model = Course
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    template_name = 'academics/course-single.html'
    model = Course
    context_object_name = 'course'


class ContactView(TemplateView):
    template_name= 'contact.html'
