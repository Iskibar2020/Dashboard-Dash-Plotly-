from dash import html, dcc
from data_setup import GLOBAL_MIN_POP, GLOBAL_MAX_POP, continent_options

def filters_ui():
    return html.Div([

        # Search input + button
            html.Div([
            dcc.Input(id="search-input", type="text",
                      placeholder="Type a Country Name (e.g., ‘Bangladesh’)",
                      style={"width": "300px"}),
            html.Button("Go", id="search-button", n_clicks=0),
            ], style={"float":"right","justifyContent": "right","padding": "10px", "padding-right":"0px"}),

        # Continent dropdown
        html.Div([
            dcc.Dropdown(
                id="continent-dropdown",
                options=continent_options,
                placeholder="Select a Continent to Filter",
                multi=False,
                style={"width": "300px", "color":"#0a0d16"}
            ),

            # Population range slider
        html.Div([
            html.Label("Filter by Estimated Population", style={"margin-left": "350px","color":"white"}),
            dcc.RangeSlider(
                id="population-range-slider",
                min=GLOBAL_MIN_POP, max=GLOBAL_MAX_POP, step=100000,
                value=[GLOBAL_MIN_POP, GLOBAL_MAX_POP],
                marks={
                    GLOBAL_MIN_POP: f"{GLOBAL_MIN_POP:,}",
                    GLOBAL_MAX_POP: f"{GLOBAL_MAX_POP:,}",
                },
                tooltip={"placement": "bottom", "always_visible": True},
                allowCross=False, updatemode="mouseup"
            ),
        ], style={"width": "50%", "margin": "0 auto", "padding": "0px 0"}),

            
        ]),

        
        
    ])
