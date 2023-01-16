from django.shortcuts import render

import plotly
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px
import json

# https: // www.codingwithricky.com/2019/08/28/easy-django-plotly/


def graph(request):
    x_data = [0, 1, 2, 3]
    y_data = [x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                             mode='lines', name='test',
                             opacity=0.8, marker_color='red')],
                    output_type='div', show_link=False, link_text="", include_plotlyjs=False)

    grp = px.line(x=x_data, y=y_data,)
    plot_json = json.dumps(grp, cls=plotly.utils.PlotlyJSONEncoder)
    ctx = {'plot_div': plot_div, 'plot_json': plot_json}

    return render(request, "gplot/graph.html", context=ctx)
