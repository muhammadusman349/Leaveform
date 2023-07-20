import django_filters
from .models import User,Department

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields= ["first_name","last_name","email","organization","department","created_at"]


class DepartmentFilter(django_filters.FilterSet):
    class Meta:
        model = Department
        fields= ["name","manager","created_at"]