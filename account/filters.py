import django_filters
from .models import User,Department

class UserFilter(django_filters.FilterSet):
    # first_name = django_filters.CharFilter(field_name="first_name",label="first_name",lookup_expr="icontains")
    # last_name = django_filters.CharFilter(field_name="last_name",label="last_name",lookup_expr="icontains")
    # email = django_filters.CharFilter(field_name="email",label="email",lookup_expr="icontains")
    # organization = django_filters.CharFilter(field_name="organization",label="organization",lookup_expr="exact")
    # department = django_filters.CharFilter(field_name="department",label="department",lookup_expr="exact")
    # created_at = django_filters.CharFilter(field_name="created_at",label="created_at",lookup_expr=)

    class Meta:
        model = User
        fields= ["first_name","last_name","email","organization","department","created_at"]


class DepartmentFilter(django_filters.FilterSet):

    class Meta:
        model = Department
        fields= ["name","manager","created_at"]