from django.shortcuts import render
from django.views.generic import ListView
from django.db.models.query import QuerySet
from .models import Result
from typing import Any

# Create your views here.

class ResultsListView(ListView):
    ''' View to display list of marathon results. '''

    template_name = 'marathon_analytics/results.html'
    model = Result
    context_object_name = "results"
    paginate_by = 50

    def get_queryset(self) -> QuerySet[Any]:
        ''' return the set of results '''

        # use the superclass version of the queryset
        qs = super().get_queryset() # default, return all records
        # return qs[:25] # return 25 records sfor now

        # if we have a search parameter, use it to filter the query set
        if 'city' in self.request.GET:
            city = self.request.GET['city']
            if city: # if not empty string
                qs = Result.objects.filter(city__icontain = city)
                    # icontain: insensitive Capitalization contain

        return qs
