from django.contrib import admin
from q3_row_search.models import ConditionOccurrence, DrugExposure


@admin.register(ConditionOccurrence)
class ConditionOccurrenceAdmin(admin.ModelAdmin):
    list_display = [
        "condition_occurrence_id",
        "person",
        "condition_concept_id",
        "condition_type_concept_id",
        # "condition_status_concept_id", #### concept_id
        # "condition_source_concept_id", #### concept_id
        "provider_id"
    ]
    readonly_fields = ["person"]
    list_per_page = 20


@admin.register(DrugExposure)
class DrugExposureAdmin(admin.ModelAdmin):
    list_display = [
        "drug_exposure_id",
        "person",
        "visit_occurrence",
        "drug_concept_id",
        "drug_type_concept_id",
        "drug_source_concept_id",
        # "route_concept_id", #### concept_id
        # "drug_exposure_start_date",
        # "drug_exposure_end_date",
        # "days_supply",
        # "drug_source_value",
    ]
    readonly_fields = ["person", "visit_occurrence"]
    list_per_page = 20
