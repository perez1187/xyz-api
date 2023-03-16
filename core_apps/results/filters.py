import django_filters as filters

# from .models import Result


class ResultFilter(filters.FilterSet):
    user = filters.CharFilter(field_name="nickname__player__username")

    class Meta:
        # model = Result
        fields = ["user"]