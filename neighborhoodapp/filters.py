import django_filters
from .models import Business
from django_filters import DateFilter, CharFilter
class BusinessFilter(django_filters.FilterSet):
  name = CharFilter(field_name='name', lookup_expr='icontains')
  class Meta:
    model = Business
    fields = 'name','neighborhood'
