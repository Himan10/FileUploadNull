# This py file is used for defining filters for respective models

import django_filters
from helloAPI.models import Job

# here we defined a class which contains some fields on which the filter operate on
# and a meta class to provide more information about which model and field names it uses
class JobFilter(django_filters.FilterSet):
    company = django_filters.CharFilter(lookup_expr='icontains')
    location = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model=Job
        fields=['company', 'location']