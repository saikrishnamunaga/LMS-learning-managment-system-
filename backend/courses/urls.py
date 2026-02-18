from django.urls import path
from .views import CourseListCreateView, AssignmentListCreateView, SubmissionCreateView, SubmissionListView, SubmissionDetailView

urlpatterns = [
    path('', CourseListCreateView.as_view()),
    path('assignments/', AssignmentListCreateView.as_view()),
    path('submissions/', SubmissionListView.as_view()),
    path('submissions/create/', SubmissionCreateView.as_view()),
    path('submissions/<int:pk>/', SubmissionDetailView.as_view()),
]
