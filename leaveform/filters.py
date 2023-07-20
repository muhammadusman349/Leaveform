import django_filters
from .models import LeaveForm

class LeaveFormFilter(django_filters.FilterSet):
    class Meta:
        model = LeaveForm
        fields =["leave_type","type_of_request","start_date","end_date","status"]