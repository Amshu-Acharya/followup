from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from enquiry.models import Course


class IndexView(ListView):
    template_name = 'index.html'
    model = Course
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    template_name = 'course_detail.html'
    model = Course
    context_object_name = 'course'
