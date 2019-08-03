from django.utils.text import slugify

from user.models import CustomUser

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
    slug = models.SlugField(max_length=200, unique=True)
    cost = models.PositiveIntegerField()
    duration = models.DurationField()
    syllabus = models.TextField()
    shifts = models.ManyToManyField(Shift, related_name='courses')
    image = models.ImageField(upload_to='course')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): # String Representation of instance
        return self.title

    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(self.title) != self.slug:
                self.slug = generate_unique_slug(Course, self.title)
        else:  # create
            self.slug = generate_unique_slug(Course, self.title)
        super().save(*args, **kwargs)


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

