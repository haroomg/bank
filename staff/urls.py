from django.urls import path, include
from .views import StaffView

urlpatterns = [
    path('create/', StaffView.as_view()),
]