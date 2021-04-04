from rest_framework import filters


class FieldSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        query_param = request.query_params.get('col')
        if query_param:
            if ',' in query_param:
                params = query_param.split(',')
            else:
                params = [query_param,]
            fields = view.queryset.model._meta.get_fields()
            search_cols = []
            for key in params:
                search_cols += [field.name for field in fields if key in field.name]
            if len(search_cols) > 0:
                return list(set(search_cols))
            else:
                return super(FieldSearchFilter, self).get_search_fields(view, request)
        else:
            return super(FieldSearchFilter, self).get_search_fields(view, request)
