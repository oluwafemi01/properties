from rest_framework import serializers
from properties.models import properties

class PropertiesSerializer(serializers.ModelSerializer):

    class Meta :
        model = properties
        fields = ('id','title','location','description','user','image','bathroom','room','created_date')


