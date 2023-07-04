from django.urls import path
from .views import LeaveFormView,TimeLogView



urlpatterns = [
    path("leaveformlist/",                   LeaveFormView.as_view(),       name='leaveform-listcreate-view'),
    path('leaveform/<int:id>/',              LeaveFormView.as_view(),       name='leaveform-detail-view'),
    path("timeloglist/",                     TimeLogView.as_view(),         name='timelog-listcreate-view'),
    path('timelog/<int:id>/',                TimeLogView.as_view(),         name='timelog-detail-view'),
]