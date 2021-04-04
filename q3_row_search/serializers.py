from rest_framework import serializers
from q1_simple_statistics.models import Person, VisitOccurrence, Death
from q2_concept_info.models import Concept
from q3_row_search.models import ConditionOccurrence, DrugExposure


class PersonSerializer(serializers.ModelSerializer):
    gender_concept_name = serializers.SerializerMethodField()
    race_concept_name = serializers.SerializerMethodField()
    ethnicity_concept_name = serializers.SerializerMethodField()
    gender_source_concept_name = serializers.SerializerMethodField()
    race_source_concept_name = serializers.SerializerMethodField()
    ethnicity_source_concept_name = serializers.SerializerMethodField()

    concept_q = Concept.objects.only("concept_id", "concept_name")

    def get_gender_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.gender_concept_id).concept_name
        except Exception as e:
            return None

    def get_race_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.race_concept_id).concept_name
        except Exception as e:
            return None

    def get_ethnicity_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.ethnicity_concept_id).concept_name
        except Exception as e:
            return None

    def get_gender_source_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.gender_source_concept_id).concept_name
        except Exception as e:
            return None

    def get_race_source_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.race_source_concept_id).concept_name
        except Exception as e:
            return None

    def get_ethnicity_source_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.ethnicity_source_concept_id).concept_name
        except Exception as e:
            return None

    class Meta:
        model = Person
        fields = ["person_id", "person_source_value",
                  "year_of_birth", "month_of_birth", "day_of_birth", "birth_datetime",
                  "gender_source_value", "race_source_value", "ethnicity_source_value",
                  "gender_concept_id", "gender_concept_name",
                  "race_concept_id", "race_concept_name",
                  "ethnicity_concept_id", "ethnicity_concept_name",
                  "gender_source_concept_id", "gender_source_concept_name",
                  "race_source_concept_id", "race_source_concept_name",
                  "ethnicity_source_concept_id", "ethnicity_source_concept_name",
                  "location_id", "provider_id", "care_site_id"]


class DeathSerializer(serializers.ModelSerializer):
    death_type_concept_name = serializers.SerializerMethodField()
    cause_concept_name = serializers.SerializerMethodField()
    cause_source_concept_name = serializers.SerializerMethodField()

    concept_q = Concept.objects.only("concept_id", "concept_name")

    def get_death_type_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.death_type_concept_id).concept_name
        except Exception as e:
            return None

    def get_cause_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.cause_concept_id).concept_name
        except Exception as e:
            return None

    def get_cause_source_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.cause_source_concept_id).concept_name
        except Exception as e:
            return None

    class Meta:
        model = Death
        fields = [
            "person_id", "death_date", "death_datetime",
            "death_type_concept_id", "death_type_concept_name",
            "cause_concept_id", "cause_concept_name",
            "cause_source_concept_id", "cause_source_concept_name", "cause_source_value",
        ]


class VisitSerializer(serializers.ModelSerializer):
    visit_concept_name = serializers.SerializerMethodField()
    visit_type_concept_name = serializers.SerializerMethodField()
    visit_source_concept_name = serializers.SerializerMethodField()
    admitted_from_concept_name = serializers.SerializerMethodField()
    discharge_to_concept_name = serializers.SerializerMethodField()

    concept_q = Concept.objects.only("concept_id", "concept_name")

    def get_visit_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.visit_concept_id).concept_name
        except Exception as e:
            return None

    def get_visit_type_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.visit_type_concept_id).concept_name
        except Exception as e:
            return None

    def get_visit_source_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.visit_source_concept_id).concept_name
        except Exception as e:
            return None

    def get_admitted_from_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.admitted_from_concept_id).concept_name
        except Exception as e:
            return None

    def get_discharge_to_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.discharge_to_concept_id).concept_name
        except Exception as e:
            return None

    class Meta:
        model = VisitOccurrence
        fields = [
            "visit_occurrence_id", "preceding_visit_occurrence_id",
            "person_id",
            "visit_concept_id", "visit_concept_name", "visit_source_value",
            "visit_type_concept_id", "visit_type_concept_name",
            "visit_source_concept_id", "visit_source_concept_name",
            "admitted_from_concept_id", "admitted_from_concept_name", "admitted_from_source_value",
            "discharge_to_concept_id", "discharge_to_concept_name", "discharge_to_source_value",
            "visit_start_date", "visit_start_datetime",
            "visit_end_date", "visit_end_datetime",
            "provider_id", "care_site_id",
        ]


class ConditionSerializer(serializers.ModelSerializer):
    condition_concept_name = serializers.SerializerMethodField()
    condition_type_concept_name = serializers.SerializerMethodField()
    condition_status_concept_name = serializers.SerializerMethodField()
    condition_source_concept_name = serializers.SerializerMethodField()

    concept_q = Concept.objects.only("concept_id", "concept_name")

    def get_condition_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.condition_concept_id).concept_name
        except Exception as e:
            return None

    def get_condition_type_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.condition_type_concept_id).concept_name
        except Exception as e:
            return None

    def get_condition_status_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.condition_status_concept_id).concept_name
        except Exception as e:
            return None

    def get_condition_source_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.condition_source_concept_id).concept_name
        except Exception as e:
            return None

    class Meta:
        model = ConditionOccurrence
        fields = [
            "condition_occurrence_id",
            "person_id",
            "visit_occurrence_id",
            "visit_detail_id",
            "condition_concept_id",
            "condition_concept_name",
            "condition_status_concept_id",
            "condition_status_concept_name",
            "condition_source_value",
            "condition_status_source_value",
            "condition_type_concept_id",
            "condition_type_concept_name",
            "condition_source_concept_id",
            "condition_source_concept_name",
            "condition_start_date",
            "condition_start_datetime",
            "condition_end_date",
            "condition_end_datetime",
            "stop_reason",
            "provider_id",
        ]


class DrugSerializer(serializers.ModelSerializer):
    drug_concept_name = serializers.SerializerMethodField()
    drug_type_concept_name = serializers.SerializerMethodField()
    drug_source_concept_name = serializers.SerializerMethodField()
    route_concept_name = serializers.SerializerMethodField()

    concept_q = Concept.objects.only("concept_id", "concept_name")

    def get_drug_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.drug_concept_id).concept_name
        except Exception as e:
            return None

    def get_drug_type_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.drug_type_concept_id).concept_name
        except Exception as e:
            return None

    def get_drug_source_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.drug_source_concept_id).concept_name
        except Exception as e:
            return None

    def get_route_concept_name(self, obj):
        try:
            return self.concept_q.get(concept_id=obj.route_concept_id).concept_name
        except Exception as e:
            return None

    class Meta:
        model = DrugExposure
        fields = [
            "drug_exposure_id", "person_id",
            "visit_occurrence_id", "visit_detail_id",
            "drug_concept_id", "drug_concept_name", "drug_source_value",
            "drug_type_concept_id", "drug_type_concept_name",
            "drug_source_concept_id", "drug_source_concept_name",
            "route_concept_id", "route_concept_name",
            "route_source_value", "dose_unit_source_value",
            "drug_exposure_start_date", "drug_exposure_start_datetime",
            "drug_exposure_end_date", "drug_exposure_end_datetime", "verbatim_end_date",
            "stop_reason", "refills", "quantity", "days_supply",
            "sig", "lot_number", "provider_id",
        ]
