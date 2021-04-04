from rest_framework import serializers, generics, filters
from q2_concept_info.models import Concept
from q3_row_search.filters import FieldSearchFilter


class ConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concept
        fields = '__all__'


class ConceptList(generics.ListAPIView):
    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer
    filter_backends = [FieldSearchFilter]
    search_fields = ["concept_id", "concept_name", "domain_id"]
