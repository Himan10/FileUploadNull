from rest_framework import serializers
from helloAPI.models import Job, Person

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields='__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'