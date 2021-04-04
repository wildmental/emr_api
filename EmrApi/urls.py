from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from q1_simple_statistics.views import PersonStatViewSet, VisitStatViewSet
from q2_concept_info.views import ConceptList
from q3_row_search.views import (PersonList, DeathList, VisitList,
                                 ConditionList, DrugList)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'person', PersonStatViewSet)
router.register(r'visit', VisitStatViewSet)


urlpatterns = [
    re_path('^emr_api/person/$', PersonList.as_view()),
    re_path('^emr_api/death/$', DeathList.as_view()),
    re_path('^emr_api/visit/$', VisitList.as_view()),
    re_path('^emr_api/condition/$', ConditionList.as_view()),
    re_path('^emr_api/drug/$', DrugList.as_view()),
    re_path('^emr_api/concept/$', ConceptList.as_view()),
    path('emr_api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
