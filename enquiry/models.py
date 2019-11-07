from django.utils.text import slugify

from user.models import CustomUser
from ckeditor.fields import RichTextField


from django.contrib.auth.models import User
from django.db import models


def generate_unique_slug(klass, field):
    """
    return unique slug if origin slug is exist.
    eg: `foo-bar` => `foo-bar-1`

    :param `klass` is Class model.
    :param `field` is specific field for title.
    """
    origin_slug = slugify(field)
    unique_slug = origin_slug
    numb = 1
    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = '%s-%d' % (origin_slug, numb)
        numb += 1
    return unique_slug


class Shift(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=254)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    cost = models.PositiveIntegerField()
    duration = models.CharField(max_length=50, blank=True)
    extra_information = RichTextField()
    shifts = models.ManyToManyField(Shift, through='CourseShift')
    image = models.ImageField(upload_to='course')
    created_at = models.DateTimeField(auto_now_add=True)
    excerpt = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(self.title) != self.slug:
                self.slug = generate_unique_slug(Course, self.title)
        else:  # create
            self.slug = generate_unique_slug(Course, self.title)
        super().save(*args, **kwargs)


class CourseShift(models.Model):
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name='course_shifts')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_shifts')
    seats = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{} - {}'.format(self.shift, self.course)

    @property
    def remaining_seats(self):
        return self.seats - self.students.count()

    @property
    def has_remaining_seats(self):
        return self.seats > self.students.count()


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    latest_eduation = models.CharField(max_length=200)
    preferred_eduation = models.CharField(max_length=200)

    def __str__(self):
        return self.user.get_username()


class Enquiry(models.Model):
    courses = models.ManyToManyField(Course, related_name='enquires')
    enquiry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_username()


class StudentEnrollment(models.Model):
    course = models.ForeignKey(CourseShift, related_name='students', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='enrolled_courses', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return '{}\'s  {}'.format(self.user.get_username(), self.course)
