from django import template

from enquiry.models import StudentEnrollment

register = template.Library()


@register.simple_tag
def has_already_enrolled(user, course):
    return StudentEnrollment.objects.filter(
        student__user=user,
        course_shift__course=course
    ).exists()
