from django.urls import path
from .views import LeaveFormView,LeaveFormDetailView



urlpatterns = [
    path("Leaveform/",                   LeaveFormView.as_view(),              name='leaveform'),
    path('leaveform/<int:id>/',           LeaveFormDetailView.as_view(),       name='leave-detail'),
]