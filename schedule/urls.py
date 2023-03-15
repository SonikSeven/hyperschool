from django.urls import re_path

from . import views

urlpatterns = [
    re_path("^main/?$", views.MainView.as_view(), name="main_url"),
    re_path(r"^course_details/(?P<pk>\d+)/?$", views.CourseView.as_view(), name="course_url"),
    re_path(r"^teacher_details/(?P<pk>\d+)/?$", views.TeacherView.as_view(), name="teacher_url"),
    re_path("^add_course/?$", views.ApplicationView.as_view(), name="application_url"),
]
