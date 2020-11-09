import django_filters

from .models import User

class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name",lookup_expr="icontains"),
    email = django_filters.CharFilter(field_name="email",lookup_expr="icontains")
    class Meta:
        model = User
        fields = ['name','email']