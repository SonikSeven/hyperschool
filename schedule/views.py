from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView

from . import forms
from . import models


class MainView(View):
    def get(self, request):
        form = forms.SearchForm(request.GET)
        if form.is_valid():
            title_substring = form.cleaned_data["q"]
            course_list = models.Course.objects.filter(title__contains=title_substring)
        else:
            form = forms.SearchForm()
            course_list = models.Course.objects.all()
        context = {"form": form, "course_list": course_list}
        return render(request, "schedule/main.html", context)


class CourseView(DetailView):
    model = models.Course
    context_object_name = "course"
    template_name = "schedule/course.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course_students"] = models.Student.objects.filter(course__title=self.object.title)
        return context


class TeacherView(DetailView):
    model = models.Teacher
    context_object_name = "teacher"
    template_name = "schedule/teacher.html"


class ApplicationView(CreateView):
    model = models.Student
    fields = ["name", "surname", "age"]
    template_name = "schedule/application.html"
    success_url = reverse_lazy("application_url")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.course = models.Course.objects.get(pk=self.request.GET.get('id'))
        context["course_title"] = self.course.title
        return context

    def form_valid(self, form):
        form.instance.course = self.course
        return super().form_valid(form)
