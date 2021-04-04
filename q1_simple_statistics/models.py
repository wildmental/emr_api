from django.db import models
from q2_concept_info.models import Concept
from django_postgres_timestamp_without_tz import DateTimeWithoutTZField


class Person(models.Model):
    # 데이터 식별자
    person_id = models.BigIntegerField(primary_key=True)
    person_source_value = models.CharField(null=True, blank=True, max_length=50)

    # 출생일시
    year_of_birth = models.IntegerField(null=True, blank=True)
    month_of_birth = models.IntegerField(null=True, blank=True)
    day_of_birth = models.IntegerField(null=True, blank=True)
    birth_datetime = DateTimeWithoutTZField(null=True, blank=True)

    # source_value 필드
    gender_source_value = models.CharField(null=True, blank=True, max_length=50)
    race_source_value = models.CharField(null=True, blank=True, max_length=50)
    ethnicity_source_value = models.CharField(null=True, blank=True, max_length=50)

    # concept_id 필드
    gender_concept_id = models.IntegerField(null=True, blank=True)
    race_concept_id = models.IntegerField(null=True, blank=True)
    ethnicity_concept_id = models.IntegerField(null=True, blank=True)

    # source_concept_id 필드
    gender_source_concept_id = models.IntegerField(null=True, blank=True)
    race_source_concept_id = models.IntegerField(null=True, blank=True)
    ethnicity_source_concept_id = models.IntegerField(null=True, blank=True)

    # 추가 정보 필드
    location_id = models.BigIntegerField(null=True, blank=True)
    provider_id = models.BigIntegerField(null=True, blank=True)
    care_site_id = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = "person"
        managed = False


class Death(models.Model):
    # 데이터 식별자
    person = models.OneToOneField(Person, on_delete=models.RESTRICT,
                                  related_name="death", primary_key=True)

    # 사망일자
    death_date = models.DateField(null=True, blank=True)

    # concept_id 필드
    death_type_concept_id = models.IntegerField(null=True, blank=True)
    cause_concept_id = models.BigIntegerField(null=True, blank=True)
    cause_source_concept_id = models.BigIntegerField(null=True, blank=True)

    # 추가 정보 필드
    death_datetime = DateTimeWithoutTZField(null=True, blank=True)
    cause_source_value = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "death"
        managed = False


class VisitOccurrence(models.Model):
    # 데이터 식별자
    visit_occurrence_id = models.BigIntegerField(primary_key=True)
    preceding_visit_occurrence_id = models.BigIntegerField(null=True, blank=True)
    person = models.ForeignKey(Person, on_delete=models.RESTRICT, related_name="visit")

    # 방문일시
    visit_start_date = models.DateField(null=True, blank=True)
    visit_start_datetime = DateTimeWithoutTZField(null=True, blank=True)
    visit_end_date = models.DateField(null=True, blank=True)
    visit_end_datetime = DateTimeWithoutTZField(null=True, blank=True)

    # source_value 필드
    visit_source_value = models.CharField(null=True, blank=True, max_length=50)
    admitted_from_source_value = models.CharField(null=True, blank=True, max_length=50)
    discharge_to_source_value = models.CharField(null=True, blank=True, max_length=50)

    # concept_id 필드
    visit_concept_id = models.IntegerField(null=True, blank=True)
    visit_type_concept_id = models.IntegerField(null=True, blank=True)
    visit_source_concept_id = models.IntegerField(null=True, blank=True)
    admitted_from_concept_id = models.IntegerField(null=True, blank=True)
    discharge_to_concept_id = models.IntegerField(null=True, blank=True)

    # 추가 정보 필드
    provider_id = models.BigIntegerField(null=True, blank=True)
    care_site_id = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = "visit_occurrence"
        managed = False
