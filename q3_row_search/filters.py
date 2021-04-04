from rest_framework import filters


class FieldSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        col_name = request.query_params.get('col')
        if col_name:
            return [col_name]
        return super(FieldSearchFilter, self).get_search_fields(view, request)