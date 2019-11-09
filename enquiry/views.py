from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.forms import ModelForm
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.views.generic.base import View

from enquiry.models import Course, Student, StudentEnrollment, Enquiry


class IndexView(ListView):
    template_name = 'academics/index.html'
    model = Course
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    template_name = 'academics/course-single.html'
    model = Course
    context_object_name = 'course'


class EnquiryForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['email'].label = ''
        self.fields['location'].label = ''
        self.fields['phone_number'].label = ''
        self.fields['message'].label = ''
        self.fields['courses'].label = ''
        self.fields['first_name'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['last_name'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['location'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['message'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['courses'].widget.attrs['class'] = 'form-control form-control-lg'

    class Meta:
        model = Enquiry
        fields = '__all__'


class ContactView(CreateView):
    template_name = 'academics/contact.html'
    model = Enquiry
    form_class = EnquiryForm

    def form_valid(self, form):
        messages.success(self.request, 'Your Request is Noted.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Some error occurred.')
        return super().form_invalid(form)


class CourseListView(ListView):
    template_name = 'academics/courses.html'
    context_object_name = 'courses'
    model = Course


class StudentEnrollmentView(LoginRequiredMixin, View):
    raise_exception = True

    def post(self, request, *args, **kwargs):
        course_shift = request.POST.get('shift', None)
        phone_number = request.POST.get('phone_number', '')
        education_level = request.POST.get('education_level', '')
        location = request.POST.get('location', '')

        try:
            with transaction.atomic():
                user = request.user

                student, _ = Student.objects.get_or_create(
                    user=user,
                    defaults=dict(
                        phone_number=phone_number,
                        education_level=education_level,
                        location=location
                    )
                )

                StudentEnrollment.objects.get_or_create(
                    course_shift_id=course_shift,
                    student=student
                )

                messages.success(request, 'You will enrolled successfully once the request is verified.')
        except Exception:
            messages.error(request, 'You request is not completed successfully.')
        return redirect(reverse('enquiry:index'))
