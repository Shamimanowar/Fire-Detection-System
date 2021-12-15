from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.ListCreateView.as_view()),
    path('create/<id>/', views.RetrieveUpdateDeleteView.as_view()),
]
