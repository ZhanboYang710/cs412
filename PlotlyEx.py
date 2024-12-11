import math 
import plotly
import plotly.graph_objs as go

# generate some data
x = [i/10 for i in range(100)]
y = [math.sin(v) for v in x]

# check data
print(f'x={x}')
print(f'y={y}')

# build figure and plot
fig = go.Scatter(x=x, y=y)
fig2 = go.Bar(x=x, y=y)
plotly.offline.plot({'data': [fig]})

# pie chart example
x = ['apple pie', 
        'pumpkin pie',
        'chocolate pecan pie',
        'chocolate bourbon pecan pie',
        ]
y = [
    14,
    9,
    3,
    2
    ]
fig3 = go.Pie(labels=x, values=y)
# plotly.offline.plot({'data':[fig]})
graph_div = plotly.offline.plot(
    {'data':[fig3]},
    auto_open=False,
    output_type='div',
)