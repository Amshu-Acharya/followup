from django.urls import path
from django.views.generic import TemplateView

from enquiry.views import IndexView, CourseDetailView, ContactView, StudentEnrollmentView, CourseListView

app_name = 'enquiry'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('course/<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
    path('contact', ContactView.as_view(), name='contact'),
    path('enroll', StudentEnrollmentView.as_view(), name='enroll'),
    path('admissions', TemplateView.as_view(template_name='academics/admissions.html'), name='admission'),
    path('about', TemplateView.as_view(template_name='academics/about.html'), name='about'),
    path('courses', CourseListView.as_view(), name='course_list'),
]
