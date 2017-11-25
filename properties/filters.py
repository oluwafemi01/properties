import django_filters
from .models import properties

class propertiesFilter(django_filters.FilterSet):
	location = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = properties
		fields = ['location','bathroom','room', ]
		exclude = ['image']
