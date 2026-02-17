from django.urls import path
from .views import CourseListCreateView, AssignmentListCreateView, SubmissionCreateView

urlpatterns = [
    path('', CourseListCreateView.as_view()),
    path('assignments/', AssignmentListCreateView.as_view()),
    path('submissions/', SubmissionCreateView.as_view()),
]
