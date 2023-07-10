from django.shortcuts import render
from rest_framework import viewsets
from helloAPI.models import Job, Person
from helloAPI.serializers import JobSerializer, PersonSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from helloAPI.filters import JobFilter

# Create your views here.
# this ModelViewSet provides basic crud methods like create, update etc.
class JobViewSets(viewsets.ModelViewSet):
    queryset = Job.objects.all() # Get all the objects from Database
    serializer_class = JobSerializer

    # Defining filters
    # DjangoFilterBackend allows to use filters in the URL as well (like /api/?company="xyz")
    # SearchFilter means the same except it'll operate on N number of fields but in the url
    # it'll be like (/api/company/?search="xyz")
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company', 'location']

    #def list(self, request, *args, **kwargs):
    #    json_data = request.data

    #    filter_class = self.filterset_class
    #    filter_instance = filter_class(data=json_data, queryset=self.get_queryset(), request=request)

    #    if filter_instance.is_valid():
    #        queryset = filter_instance.qs
    #    else:
    #        queryset = self.get_queryset()

    #    serializerData = JobSerializer(queryset, many=True)
    #    return Response(serializerData.data)

class PersonViewSets(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    # Using this method we can find out which jobs a person has applied so far
    @action(detail=True, methods=['get'])
    def jobs(self, request, pk=None): #pk here means primary key
        # here we get the data
        try:
            personData=Person.objects.get(pk=pk)
            jobsData=Job.objects.filter(person=personData)

            # here we serialize the data, for comm.
            serializedJobsData = JobSerializer(jobsData, many=True, context={"request": request})
            return Response(serializedJobsData.data)
        except ObjectDoesNotExist:
            return Response({"message": f"person id '{pk}' doesn't exist"})
