from django.urls import path
from .views import LeaveFormView,TimeLogView,CommentView



urlpatterns = [
    path("leaveformlist/",                   LeaveFormView.as_view(),       name='leaveform-listcreate-view'),
    path('leaveform/<int:id>/',              LeaveFormView.as_view(),       name='leaveform-detail-view'),
    path("timeloglist/",                     TimeLogView.as_view(),         name='timelog-listcreate-view'),
    path('timelog/<int:id>/',                TimeLogView.as_view(),         name='timelog-detail-view'),
    path("comment/",                         CommentView.as_view(),         name='comment-listcreate-view'),
    path('comment/<int:id>/',                CommentView.as_view(),         name='comment-detail-view'),
]