import django_filters
from .models import LeaveForm

class LeaveFormFilter(django_filters.FilterSet):
    # leave_type= django_filters.CharFilter(field_name="leave_type",label="leave_type",lookup_expr="exact")
    # type_of_request= django_filters.CharFilter(field_name="type_of_request",label="type_of_request",lookup_expr="exact")
    # start_date= django_filters.CharFilter(field_name="start_date",label="start_date",lookup_expr="exact")
    # end_date= django_filters.CharFilter(field_name="end_date",label="end_date",lookup_expr="gte")
    # status= django_filters.CharFilter(field_name="status",label="status",lookup_expr="lte")


    class Meta:
        model = LeaveForm
        fields =["leave_type","type_of_request","start_date","end_date","status"]