from django.urls import path

from enquiry.views import IndexView, CourseDetailView, ContactView

app_name = 'enquiry'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('course/<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
    path('contact', ContactView.as_view(),name='contact')
]
