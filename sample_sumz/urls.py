from django.urls import path
from sample_sumz import views

urlpatterns = [
    path("", views.AddQuestions.as_view(), name="sample_file")
]