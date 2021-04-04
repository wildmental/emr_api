from django.contrib import admin
from q2_concept_info.models import Concept


@admin.register(Concept)
class ConceptAdmin(admin.ModelAdmin):
    list_display = [
        "concept_id",
        "concept_name",
        "domain_id",
        "vocabulary_id",
        "concept_class_id",
        "standard_concept",
        "concept_code",
        "valid_start_date",
        "valid_end_date",
        "invalid_reason"
    ]
    list_per_page = 20
