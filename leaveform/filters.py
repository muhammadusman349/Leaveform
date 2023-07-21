import django_filters
from .models import LeaveForm

class LeaveFormFilter(django_filters.FilterSet):
    leave_type = django_filters.CharFilter(field_name="leave_type",lookup_expr="iexact")
    type_of_request = django_filters.CharFilter(field_name="type_of_request",lookup_expr="iexact")
    status = django_filters.CharFilter(field_name="status",lookup_expr="iexact")
    start_date= django_filters.CharFilter(field_name="start_date",lookup_expr="gte")
    end_date= django_filters.CharFilter(field_name="end_date",lookup_expr="lte")

    class Meta:
        model = LeaveForm
        fields =["leave_type","type_of_request","status","start_date","end_date"]