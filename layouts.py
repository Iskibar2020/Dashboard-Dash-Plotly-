from dash import html
from components.filters import filters_ui
from components.charts import charts_ui
from components.map_component import map_ui
from components.table import table_ui

def init_layout(app):
    app.layout = html.Div([
    html.Div(filters_ui(), className="filters-section"),
    html.Div(map_ui(), className="map-section"),
    html.Div(charts_ui(), className="charts-section"),
    html.Div(table_ui(), className="table-section")
],
className="dashboard-container"

)

