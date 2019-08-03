from django.urls import path

from enquiry.views import IndexView, CourseDetailView

app_name = 'enquiry'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('course/<slug:slug>/', CourseDetailView.as_view(), name='course_detail')
]

# path ma k kaha ayo bhane k load garney khali ayo bhane index aune bhayo
