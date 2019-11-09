from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.base import View

from enquiry.models import Course, Student, StudentEnrollment


class IndexView(ListView):
    template_name = 'academics/index.html'
    model = Course
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    template_name = 'academics/course-single.html'
    model = Course
    context_object_name = 'course'


class ContactView(TemplateView):
    template_name = 'academics/contact.html'


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
