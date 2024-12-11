from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models.query import QuerySet
from .models import Result
from typing import Any, Dict

import plotly
import plotly.graph_objs as go

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
                qs = Result.objects.filter(city__icontains = city)
                    # icontain: insensitive Capitalization contain

        return qs

class ResultDetailView(DetailView):
    '''Display a single Result on it's own page.'''

    template_name = 'marathon_analytics/result_detail.html'
    model = Result
    context_object_name = "r"

    # implementing methods...
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        # get the superclass version of context
        context = super().get_context_data(**kwargs)
        r = context['r'] # obtain the single Result instance

        # get data: half_marathon splits
        first_half_seconds = (r.time_half1.hour * 3600 +
                            r.time_half1.minute * 60 +
                            r.time_half1.second)

        second_half_seconds = (r.time_half2.hour * 3600 +
                            r.time_half2.minute * 60 +
                            r.time_half2.second)                   

        # build a pie chart
        x = ['first half time', 'second half time']
        y = [first_half_seconds, second_half_seconds]
        print(f'x={x}')
        print(f'y={y}')

        fig = go.Pie(labels=x, values=y)
        pie_div = plotly.offline.plot({'data':[fig]},
                                        auto_open=False,
                                        output_type='div')

        # add the pie chart to the context
        context['pie_div'] = pie_div

        # create a bar chart with th ebumebr of runners passed and who passed by 
        x = [f'runners passed by {r.first_name}',
            f'runners who passed {r.first_name}']
        y = [r.get_runners_passed(),
            r.get_runners_passed_by()]
        print(f'x={x}')
        print(f'y={y}')
        fig = go.Bar(x=x, y=y)
        bar_div = plotly.offline.plto({'data': [fig]},
                                        auto_open=False,
                                        output_type='div',)
        # add this to the context data for use in the template
        context['bar_div'] = bar_div