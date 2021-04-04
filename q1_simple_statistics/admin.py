from django.contrib import admin
from q1_simple_statistics.models import Person, Death, VisitOccurrence


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = [
        "person_id", "year_of_birth",
        "gender_source_value", "race_source_value",
        "ethnicity_source_value"
    ]
    list_per_page = 20


@admin.register(Death)
class DeathAdmin(admin.ModelAdmin):
    list_display = ["person", "death_date"]
    list_per_page = 20


@admin.register(VisitOccurrence)
class VisitOccurrenceAdmin(admin.ModelAdmin):
    list_display = [
        "visit_occurrence_id",
        "preceding_visit_occurrence_id",
        "person_id",
        "visit_type_concept_id",
        "visit_start_date",
        "visit_end_date",
        "visit_source_value"
    ]
    readonly_fields = ["person"]
    list_per_page = 20
