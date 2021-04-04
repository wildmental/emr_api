from datetime import datetime
from django.db.models import Count
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from q1_simple_statistics.models import Person, VisitOccurrence, Death
from q2_concept_info.models import Concept


class PersonStatViewSet(viewsets.GenericViewSet):
    queryset = Person.objects.all()

    @action(detail=False, methods=["GET"])
    def stat(self, request):
        q = self.queryset.only("gender_source_value", "gender_concept_id", "race_source_value", "race_concept_id",
                               "ethnicity_source_value", "ethnicity_concept_id")
        total = q.count()
        per_gender = [{gender_cnts["gender_source_value"]: gender_cnts["gender_cnt"]}
                      for gender_cnts in q.values("gender_source_value", "gender_concept_id")
                                         .annotate(gender_cnt=Count("gender_concept_id"))
                                         .order_by("-gender_cnt")]
        per_race = [{race_cnts["race_source_value"]: race_cnts["race_cnt"]}
                    for race_cnts in q.values("race_source_value", "race_concept_id")
                                     .annotate(race_cnt=Count("race_concept_id"))
                                     .order_by("-race_cnt")]
        per_ethnic = [{ethnic_cnts["ethnicity_source_value"]: ethnic_cnts["ethnic_cnt"]}
                      for ethnic_cnts in q.values("ethnicity_source_value", "ethnicity_concept_id")
                                         .annotate(ethnic_cnt=Count("ethnicity_concept_id"))
                                         .order_by("-ethnic_cnt")]
        death = Death.objects.count()
        response_data = {"total patients": total,
                         "patients per gender": per_gender,
                         "patients per race": per_race,
                         "patients per ethnic": per_ethnic,
                         "number of death": death}
        return Response(response_data, status=status.HTTP_200_OK)


class VisitStatViewSet(viewsets.GenericViewSet):
    queryset = VisitOccurrence.objects.select_related("person")\
        .only("person__gender_source_value", "person__gender_concept_id", "person__race_source_value",
              "person__race_concept_id", "person__ethnicity_source_value", "person__ethnicity_concept_id",
              "person__year_of_birth")

    @action(detail=False, methods=["GET"])
    def stat(self, request):
        q = self.queryset
        q2 = Concept.objects.only("concept_name")
        per_type = [{q2.filter(concept_id=type_cnts["visit_concept_id"])[0].concept_name: type_cnts["type_cnt"]}
                    for type_cnts in q.values("visit_concept_id")
                                      .annotate(type_cnt=Count("visit_concept_id"))
                                      .order_by("-type_cnt")]
        per_gender = [{gender_cnt["person__gender_source_value"]: gender_cnt["gender_cnt"]}
                      for gender_cnt in q.values("person__gender_source_value", "person__gender_concept_id")
                                         .order_by("person__gender_concept_id")
                                         .annotate(gender_cnt=Count("person__gender_concept_id"))]
        per_race = [{race_cnts["person__race_source_value"]: race_cnts["race_cnt"]}
                    for race_cnts in q.values("person__race_source_value", "person__race_concept_id")
                                     .annotate(race_cnt=Count("person__race_concept_id"))
                                     .order_by("-race_cnt")]
        per_ethnic = [{ethnic_cnts["person__ethnicity_source_value"]: ethnic_cnts["ethnic_cnt"]}
                      for ethnic_cnts in q.values("person__ethnicity_source_value", "person__ethnicity_concept_id")
                                          .annotate(ethnic_cnt=Count("person__ethnicity_concept_id"))
                                          .order_by("-ethnic_cnt")]
        per_age_group = []
        this_year = datetime.now().year
        max_age_year = Person.objects.only("year_of_birth").order_by("year_of_birth")[0].year_of_birth
        max_group_gap = round((this_year - max_age_year)/10)*10
        for age_group, year_interval_10 in zip(range(max_group_gap, -1, -10),
                                               range(this_year-max_group_gap, this_year+1, 10)):
            cnt = q.values("person__year_of_birth").filter(person__year_of_birth__lte=year_interval_10)\
                   .filter(person__year_of_birth__gt=year_interval_10-10).aggregate(Count("person__year_of_birth"))
            per_age_group.append({f"{age_group}y to {age_group+9}y": cnt['person__year_of_birth__count']})
        response_data = {"visits per type": per_type,
                         "visits per gender": per_gender,
                         "visits per race": per_race,
                         "visits per ethnic": per_ethnic,
                         "visits per age group": per_age_group}
        return Response(response_data, status=status.HTTP_200_OK)


