from django.urls import path

from . import views

app_name = "school"

urlpatterns = [
    path("", views.SchoolView.as_view(), name="list-schools"),
    path("student/", views.StudentView.as_view(), name="create-student"),
    path("student/<int:pk>/", views.StudentRetrieveView.as_view(), name="list-student"),
]
