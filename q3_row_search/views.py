from rest_framework import generics
from q1_simple_statistics.models import Person, Death, VisitOccurrence
from q3_row_search.models import ConditionOccurrence, DrugExposure
from q3_row_search.serializers import (PersonSerializer, DeathSerializer, VisitSerializer,
                                       ConditionSerializer, DrugSerializer)
from q3_row_search.filters import FieldSearchFilter


class PersonList(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [FieldSearchFilter]
    search_fields = []


class DeathList(generics.ListAPIView):
    queryset = Death.objects.all()
    serializer_class = DeathSerializer
    filter_backends = [FieldSearchFilter]
    search_fields = []


class VisitList(generics.ListAPIView):
    queryset = VisitOccurrence.objects.all()
    serializer_class = VisitSerializer
    filter_backends = [FieldSearchFilter]
    search_fields = []


class ConditionList(generics.ListAPIView):
    queryset = ConditionOccurrence.objects.all()
    serializer_class = ConditionSerializer
    filter_backends = [FieldSearchFilter]
    search_fields = []


class DrugList(generics.ListAPIView):
    queryset = DrugExposure.objects.all()
    serializer_class = DrugSerializer
    filter_backends = [FieldSearchFilter]
    search_fields = []