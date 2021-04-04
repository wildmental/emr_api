from django.db import models


class Concept(models.Model):
    # 데이터 식별자
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(null=True, blank=True, max_length=255)
    domain_id = models.CharField(null=True, blank=True, max_length=20)
    vocabulary_id = models.CharField(null=True, blank=True, max_length=20)
    concept_class_id = models.CharField(null=True, blank=True, max_length=20)
    standard_concept = models.CharField(null=True, blank=True, max_length=1)
    concept_code = models.CharField(null=True, blank=True, max_length=50)

    # 유효기간
    valid_start_date = models.DateField(null=True, blank=True)
    valid_end_date = models.DateField(null=True, blank=True)

    # 파기 이유
    invalid_reason = models.CharField(null=True, blank=True, max_length=1)

    class Meta:
        db_table = "concept"
        managed = False
