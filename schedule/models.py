from django.db import models
from django.urls import reverse


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField()
    about = models.TextField()

    def get_absolute_url(self):
        return reverse("teacher_url", kwargs={"pk": self.pk})


class Course(models.Model):
    title = models.CharField(max_length=255)
    info = models.TextField()
    duration_months = models.IntegerField()
    price = models.IntegerField()
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("course_url", kwargs={"pk": self.pk})


class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField()
    course = models.ManyToManyField(Course)
