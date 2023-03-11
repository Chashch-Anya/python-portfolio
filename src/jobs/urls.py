from django.urls import path

from jobs.views import IndexJobsListView
from jobs.views import DetailJobsListView

urlpatterns = [
    path("", IndexJobsListView.as_view(), name="jobs"),
    path("<int:pk>/", DetailJobsListView.as_view(), name="job"),
]