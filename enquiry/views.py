from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from enquiry.models import Course


class IndexView(ListView):
    template_name = 'index.html'
    model = Course
    context_object_name = 'courses'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        ctx['login_form'] = AuthenticationForm()
        ctx['registration_form'] = UserCreationForm()
        return ctx


class CourseDetailView(DetailView):
    template_name = 'course_detail.html'
    model = Course
    context_object_name = 'course'

class ContactView(TemplateView):
    template_name= 'contact.html'
