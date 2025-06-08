# callbacks.py
from dash import Input, Output, State
from geopy.geocoders import Nominatim
import plotly.express as px
import plotly.io as pio
import data_setup
from shapely.geometry import shape
from shapely.ops import unary_union

# Safe Plotly template
pio.templates.default = "plotly_white"

def register_callbacks(app):

    # ─── 1️⃣ Update ONLY the GeoJSON data ───────────────────────────────
    @app.callback(
        Output("geojson", "data"),
        Input("population-range-slider", "value"),
        Input("continent-dropdown", "value"),
        Input("search-input", "value")
    )
    def update_geojson(pop_range, continent, search_value):
        # filter DataFrame
        df = data_setup.df[
            (data_setup.df["pop_est"] >= pop_range[0]) &
            (data_setup.df["pop_est"] <= pop_range[1])
        ]
        if continent:
            df = df[df["continent"] == continent]
        if search_value:
            df = df[df["name"].str.contains(search_value, case=False, na=False)]

        # build new GeoJSON
        filtered_geojson = {
            "type": "FeatureCollection",
            "features": [
                feat for feat in data_setup.gj["features"]
                if feat.get("properties", {}).get("name") in df["name"].values
            ]
        }

        if not df.empty:
            geometries = [shape(feat["geometry"]) for feat in filtered_geojson["features"]]
            combined = unary_union(geometries)
            minx, miny, maxx, maxy = combined.bounds
            new_bounds = [[miny, minx], [maxy, maxx]]
       

        return filtered_geojson

    # ─── 2️⃣ Update Charts & Table ONLY ─────────────────────────────────
    @app.callback(
        Output("bar-chart", "figure"),
        Output("pie-chart", "figure"),
        Output("scatter-chart", "figure"),
        Output("bubble-chart", "figure"),
        Output("attribute-table", "data"),
        Input("population-range-slider", "value"),
        Input("continent-dropdown", "value"),
        Input("search-input", "value")
    )
    def update_dashboard(pop_range, continent, search_value):
        palette = ["#0a0d16", "#05172f", "#2c3c4c", "#2d3c4d", "#2f302b", "#525453"]

        # same filtering logic
        df = data_setup.df[
            (data_setup.df["pop_est"] >= pop_range[0]) &
            (data_setup.df["pop_est"] <= pop_range[1])
        ]
        if continent:
            df = df[df["continent"] == continent]
        if search_value:
            df = df[df["name"].str.contains(search_value, case=False, na=False)]

        # bar chart
        bar_df = df["subregion"].value_counts().reset_index()
        bar_df.columns = ["subregion", "count"]
        bar_fig = px.bar(
            bar_df, x="subregion", y="count",
            title="Subregion Counts",
            color="subregion",
            color_discrete_sequence=palette
        )
        bar_fig.update_layout(showlegend=False,
                              clickmode="event+select") 
        

        # pie chart
        pie_df = df["income_grp"].value_counts().reset_index()
        pie_df.columns = ["income_grp", "count"]
        pie_fig = px.pie(pie_df, names="income_grp", values="count",
                         title="Income Group Distribution",
                         color_discrete_sequence=palette)

        # scatter chart
        scatter_fig = px.scatter(df, x="pop_est", y="gdp_md_est",
                                 hover_name="name",
                                 labels={"pop_est": "Population", "gdp_md_est": "GDP (Million USD)"},
                                 title="Population vs GDP")
        scatter_fig.update_traces(marker=dict(color=palette[0]))

        # bubble chart
        bubble_fig = px.scatter(df, x="longitude", y="latitude",
                                size="pop_est", color="gdp_md_est",
                                hover_name="name",
                                labels={"longitude": "Longitude", "latitude": "Latitude"},
                                title="Country Locations (Population & GDP)",
                                color_continuous_scale=palette)

        # table data
        table_data = df.to_dict("records")

        return bar_fig, pie_fig, scatter_fig, bubble_fig, table_data

    # ─── 3️⃣ Geocode & Recenter ───────────────────────────────────────────
    @app.callback(
        Output("boundary-map", "center"),
        Output("boundary-map", "zoom"),
        Input("search-button", "n_clicks"),
        State("search-input", "value"),
        prevent_initial_call=True
    )
    def geocode_and_center(n_clicks, location_name):
        if not location_name:
            return [20, 0], 2
        geolocator = Nominatim(user_agent="dash-app")
        loc = geolocator.geocode(location_name)
        if loc:
            return [loc.latitude, loc.longitude], 5
        return [20, 0], 2
