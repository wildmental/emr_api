# EMR_API
_의료데이터 API : API for Electronic Medical Record service_

## 본 API를 테스트하기 위해서는 아래의 순서를 따른다.

1. python 3.9 버전 이상, pip 최신 버전 설치 확인

2. Git clone 및 가상환경 생성 후 requirenments 파일로 라이브러리 설치

3. python manage.py createsuperuser 커맨드로 서버 어드민 계정 생성

4. djnago 프로젝트 내 settings.py에 PostgreSQL DB 연결

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': '',
                'USER': '',
                'PASSWORD': '',
                'HOST': '',
                'PORT': '5432',
            }
        }
             
5. http://HOST-ADDRESS-HERE/admin/ 주소에서 생성된 어드민 계정 및 데이터 테이블 임포트 확인

6. 프로젝트 루트에서 python manage.py runserver 명령으로 서버 실행 후 브라우저에서 테스트

### 본 문서에 다룬 모든 API 호출은 Django restframework에서 제공하는 Browsable API View를 제공한다.
    
  참조 링크 : https://www.django-rest-framework.org/topics/browsable-api/
  
    Browsable View가 아닌 JSON 응답이 필요한 경우 ?format=json 파라미터 값을 추가한다.

### 본 API는 다음과 같은 도메인의 의료 데이터를 다룬다.
        환자(person), 사망(death), 방문(visit_occurrence), 진단(condition_occurrence), 처방(drug_exposure)

### 본 API의 호출 패턴은 다음과 같다.

1. 각 도메인 데이터를 리스트 형태로 호출

        [환자 리스트] emr_api/person/
        [사망 리스트] emr_api/death/
        [방문 리스트] emr_api/visit/
        [진단 리스트] emr_api/condition/
        [처방 리스트] emr_api/drug/


     - 기본적인 페이징이 적용되어 있음 (페이지당 20개 레코드 조회)

     - 파라미터로 검색이 가능하다 : col(검색할 컬럼 지정), search(검색 키워드 입력), <key>위치에 검색할 키 입력
     
        [환자 테이블 - 컬럼 지정 검색] emr_api/person/?col=<key>&search=<key>
        [사망 테이블 - 컬럼 지정 검색] emr_api/death/?col=<key>&search=<key>
        [방문 테이블 - 컬럼 지정 검색] emr_api/visit/?col=<key>&search=<key>
        [진단 테이블 - 컬럼 지정 검색] emr_api/condition/?col=<key>&search=<key>
        [처방 테이블 - 컬럼 지정 검색] emr_api/drug/?col=<key>&search=<key>
     
       - 검색 예시
       
         http://HOST-ADDRESS-HERE/emr_api/person/?col=year_of_birth&search=1990

                검색 동작 설명 : person 테이블의 year_of_birth컬럼에 대해 1990의 값을 갖는 모든 행 조회
         
         http://HOST-ADDRESS-HERE/emr_api/person/?col=year_of_birth&search=1990&ordering

                검색 동작 설명 : person 테이블의 year_of_birth컬럼에 대해 1990의 값을 갖는 모든 행 조회
     
     - _**검색 컬럼(col)과 검색할 키워드(search) 모두 부분일치에 대해 동일한 파라미터를 사용해 키워드 검색이 가능하다.**_
       _**검색할 컬럼에는 여러개의 키워드를 입력할 수 있다.**_
     
       - 복수의 컬럼 패턴 & 부분일치 검색 예시
       
       
         http://HOST-ADDRESS-HERE/emr_api/drug/?col=date,source&search=2020-06

                검색 동작 설명 : drug 테이블 내 date, source 문자열을 포함한 컬럼들에서 2020-06 값을 포함하는 모든 행 조회
     
     - 응답 예시 (복수 컬럼에 대한 부분일치 검색 : /emr_api/drug/?col=date,source&search=2020-06 에 대한 응답)
     
        - 데이터 리스트 호출의 모든 응답은 조회된 데이터 총 수(count), 다음페이지 링크(next), 이전 페이지 링크(previous), 현재 페이지의 결과 데이터(result)를 포함한다.
     
                  {
                   "count": 165,
                   "next": "http://HOST-ADDRESS-HERE/emr_api/drug/?col=date%2Csource&limit=20&offset=20&search=2020-06",
                   "previous": null,
                   "results": [
                       {
                        "drug_exposure_id": 12836021,
                        "person_id": 4915,
                        "visit_occurrence_id": 44873681,
                        "visit_detail_id": 0,
                        "drug_concept_id": 19075001,
                        "drug_concept_name": "cefuroxime 250 MG Oral Tablet",
                        "drug_source_value": "309097",
                        "drug_type_concept_id": 38000177,
                        "drug_type_concept_name": "Prescription written",
                        "drug_source_concept_id": 19075001,
                        "drug_source_concept_name": "cefuroxime 250 MG Oral Tablet",
                        "route_concept_id": 0,
                        "route_concept_name": "No matching concept",
                        "route_source_value": null,
                        "dose_unit_source_value": null,
                        "drug_exposure_start_date": "2020-05-29",
                        "drug_exposure_start_datetime": "2020-05-29T02:42:53Z",
                        "drug_exposure_end_date": "2020-06-12",
                        "drug_exposure_end_datetime": "2020-06-12T02:42:53Z",
                        "verbatim_end_date": "2020-06-12",
                        "stop_reason": null,
                        "refills": 0,
                        "quantity": "0.0000000000",
                        "days_supply": 14,
                        "sig": null,
                        "lot_number": "0",
                        "provider_id": 0
                        }, ..... ]
                   }
     
     - 유효하지 않은 검색 파라미터 전달시 응답
     
        - 유효하지 않은 검색 호출 예시
        
          
          http://HOST-ADDRESS-HERE/emr_api/person/?hahaha=aaa
          
                유효한 호출 패턴에 대해 col, search 이외의 파라미터가 전달된 경우 이를 무시하고 기본 조회
                (파라미터가 전달되지 않았을 때와 동일)
          
          http://HOST-ADDRESS-HERE/emr_api/person/?search=aaa
        
                col 파라미터 없이 search 파라미터만 전달된 경우에도 검색할 컬럼이 없기 때문에 기본 조회만 수행
          
        - 응답예시 (유효하지 않은 파라미터 : /emr_api/person/?hahaha=aaa 에 대한 응답)
     
                  {
                    "count": 1000,
                    "next": "http://HOST-ADDRESS-HERE/emr_api/person/?hahaha=aaa&limit=20&offset=20",
                    "previous": null,
                    "results": [
                        {
                            "person_id": 402435,
                            "person_source_value": "a434e3bf-7720-4612-8d18-e274e199f4fd",
                            "year_of_birth": 1997,
                            "month_of_birth": 4,
                            "day_of_birth": 18,
                            "birth_datetime": "1997-04-18T00:00:00Z",
                            "gender_source_value": "F",
                            "race_source_value": "white",
                            "ethnicity_source_value": "hispanic",
                            "gender_concept_id": 8532,
                            "gender_concept_name": "FEMALE",
                            "race_concept_id": 8527,
                            "race_concept_name": "White",
                            "ethnicity_concept_id": 0,
                            "ethnicity_concept_name": "No matching concept",
                            "gender_source_concept_id": 0,
                            "gender_source_concept_name": "No matching concept",
                            "race_source_concept_id": 0,
                            "race_source_concept_name": "No matching concept",
                            "ethnicity_source_concept_id": 0,
                            "ethnicity_source_concept_name": "No matching concept",
                            "location_id": null,
                            "provider_id": null,
                            "care_site_id": null
                        }, ......]
                   }
  
2. 간단한 통계 조회  
  
     - 환자와 방문 테이블에 대해서는 아래 주소로 간단한 통계를 조회할 수 있다. (검색 또는 추가 파라미터 없음)
     
            emr_api/person/stat/
            emr_api/visit/stat/
  
     - 응답 예시 (방문 통계 조회 : emr_api/visit/stat/에 대한 응답)

        - 방문 유형별, 성별, 인종별, 민족별, 방문시 연령대(10세 단위)별, 현재 연령대(10세 단위) 별 방문 수 통계를 조회

                 {
                      "visits per type": {
                          "Outpatient Visit": 37026,
                          "Emergency Room Visit": 3475,
                          "Inpatient Visit": 1309
                      },
                      "visits per gender": {
                          "M": 22503,
                          "F": 19307
                      },
                      "visits per race": {
                          "white": 35487,
                          "black": 3326,
                          "asian": 2826,
                          "native": 89,
                          "other": 82
                      },
                      "visits per ethnic": {
                          "nonhispanic": 36981,
                          "hispanic": 4829
                      },
                      "visits per age group when the visit occurred": {
                          "0y to 9y": 3225,
                          "40y to 49y": 5825,
                          "50y to 59y": 6023,
                          "60y to 69y": 4678,
                          "70y to 79y": 3587,
                          "10y to 19y": 4738,
                          "20y to 29y": 5509,
                          "30y to 39y": 5645,
                          "80y to 89y": 1658,
                          "90y to 99y": 838,
                          "100y to 109y": 84
                      },
                      "visits per current age group": {
                          "110y to 119y": 553,
                          "100y to 109y": 3303,
                          "90y to 99y": 4210,
                          "80y to 89y": 3623,
                          "70y to 79y": 4003,
                          "60y to 69y": 5023,
                          "50y to 59y": 6141,
                          "40y to 49y": 4167,
                          "30y to 39y": 3376,
                          "20y to 29y": 3867,
                          "10y to 19y": 2390,
                          "0y to 9y": 1154
                      }
                  }
  
3. 개념 사전(concept) 검색

     - 개념 사전 검색은 1번의 테이블 행 조회와 기본적으로 동일하나, col 파라미터 없이 기본 검색 호출이 가능하다.
     
            [개념 리스트] emr_api/concept/
            [기본 검색] emr_api/concept/?search=release
            [컬럼 지정 검색] emr_api/concept/?col=_id&search=2733333
            
  
     - 응답 예시 (기본 검색 : /emr_api/concept/?search=release 에 대한 응답)

        - 기본 검색 컬럼인 concept_id, concept_name, domain_id에 대해 조회

                 {
                    "count": 289051,
                    "next": "http://127.0.0.1:8000/emr_api/concept/?limit=20&offset=20&search=release",
                    "previous": null,
                    "results": [
                        {
                            "concept_id": 45414934,
                            "concept_name": "lovastatin-niacin 40 mg-1000 mg oral tablet, extended release",
                            "domain_id": "Drug",
                            "vocabulary_id": "Multum",
                            "concept_class_id": "Multum",
                            "standard_concept": null,
                            "concept_code": "16775",
                            "valid_start_date": "1970-01-01",
                            "valid_end_date": "2099-12-31",
                            "invalid_reason": null
                        }, ..... ]
                   }
   
