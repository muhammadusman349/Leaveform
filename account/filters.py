import django_filters
from .models import User,Department

class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(field_name="First Name",lookup_expr="icontains")
    last_name = django_filters.CharFilter(field_name="Last Name",lookup_expr="icontains")
    email = django_filters.CharFilter(field_name="Email",lookup_expr="icontains")
    organization = django_filters.CharFilter(field_name="Organization",lookup_expr="exact")
    department = django_filters.CharFilter(field_name="Department",lookup_expr="exact")

    class Meta:
        model = User
        fields= ["first_name","last_name","email","organization","department","created_at"]


class DepartmentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="Name",lookup_expr="icontains")
    manager = django_filters.CharFilter(field_name="Manager",lookup_expr="exact")
    class Meta:
        model = Department
        fields= ["name","manager","created_at"]