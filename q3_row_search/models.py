from django.db import models
from q1_simple_statistics.models import Person, VisitOccurrence
from django_postgres_timestamp_without_tz import DateTimeWithoutTZField


class ConditionOccurrence(models.Model):
    # 데이터 식별자
    condition_occurrence_id = models.BigIntegerField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.RESTRICT, related_name="condition")

    # 방문 정보
    visit_occurrence_id = models.BigIntegerField(null=True, blank=True)
    visit_detail_id = models.BigIntegerField(null=True, blank=True)

    # source_value 필드
    condition_source_value = models.CharField(null=True, blank=True, max_length=50)
    condition_status_source_value = models.CharField(null=True, blank=True, max_length=50)
    # 유사 source_value 필드
    stop_reason = models.CharField(null=True, blank=True, max_length=20)

    # concept_id 필드
    condition_concept_id = models.IntegerField(null=True, blank=True)
    condition_type_concept_id = models.IntegerField(null=True, blank=True)
    condition_status_concept_id = models.IntegerField(null=True, blank=True)
    condition_source_concept_id = models.IntegerField(null=True, blank=True)

    # 진단 날짜
    condition_start_date = models.DateField(null=True, blank=True)
    condition_start_datetime = DateTimeWithoutTZField(null=True, blank=True)
    condition_end_date = models.DateField(null=True, blank=True)
    condition_end_datetime = DateTimeWithoutTZField(null=True, blank=True)

    # 추가 정보 필드
    provider_id = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = "condition_occurrence"
        managed = False


class DrugExposure(models.Model):
    # 데이터 식별자
    drug_exposure_id = models.BigIntegerField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.RESTRICT, related_name="drug")

    # 방문정보
    visit_occurrence = models.ForeignKey(VisitOccurrence, on_delete=models.RESTRICT, related_name="drug")
    visit_detail_id = models.BigIntegerField(null=True, blank=True)

    # 처방일시
    drug_exposure_start_date = models.DateField(null=True, blank=True)
    drug_exposure_start_datetime = DateTimeWithoutTZField(null=True, blank=True)
    drug_exposure_end_date = models.DateField(null=True, blank=True)
    drug_exposure_end_datetime = DateTimeWithoutTZField(null=True, blank=True)
    verbatim_end_date = models.DateField(null=True, blank=True)

    # source_value 필드
    drug_source_value = models.CharField(null=True, blank=True, max_length=50)
    route_source_value = models.CharField(null=True, blank=True, max_length=50)
    dose_unit_source_value = models.CharField(null=True, blank=True, max_length=50)
    # 유사 source_value 필드
    stop_reason = models.CharField(null=True, blank=True, max_length=20)
    refills = models.IntegerField(null=True, blank=True)
    quantity = models.DecimalField(null=True, blank=True, decimal_places=10, max_digits=100)
    days_supply = models.IntegerField(null=True, blank=True)
    sig = models.TextField(null=True, blank=True)
    lot_number = models.CharField(null=True, blank=True, max_length=50)

    # concept_id 필드
    drug_concept_id = models.IntegerField(null=True, blank=True)
    drug_type_concept_id = models.IntegerField(null=True, blank=True)
    drug_source_concept_id = models.IntegerField(null=True, blank=True)
    route_concept_id = models.IntegerField(null=True, blank=True)

    # 추가 정보 필드
    provider_id = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = "drug_exposure"
        managed = False
