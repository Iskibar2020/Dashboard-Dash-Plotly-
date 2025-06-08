# charts_ui.py
from dash import dcc, html

def charts_ui():
    cfg = {
        "staticPlot": False,
        "displayModeBar": True,
        "scrollZoom": True,
        "displaylogo": False,
    }
    return html.Div([
        html.Div([
            dcc.Graph(id='bar-chart', config=cfg),
            dcc.Graph(id='pie-chart', config=cfg),
        ]),
        html.Div([
            dcc.Graph(id='scatter-chart', config=cfg),
            dcc.Graph(id='bubble-chart', config=cfg),
        ]),
    ])
