from dash import dash_table
from data_setup import df

def table_ui():
    return dash_table.DataTable(
        id="attribute-table",
        columns=[
            {"name": "Country Name", "id": "name"},
            {"name": "Continent", "id": "continent"},  
            {"name": "Subregion", "id": "subregion"},
            {"name": "Population Estimate", "id": "pop_est"},
            {"name": "GDP (Million USD)", "id": "gdp_md_est"},           
            {"name": "Income Group", "id": "income_grp"},
            {"name": "Latitude", "id": "latitude"},
            {"name": "Longitude", "id": "longitude"},
        ],
        data=df.to_dict("records"),
        page_size=10,
        filter_action="native",
        sort_action="native",
        
        # Add styling below:
        style_header={
            'backgroundColor': '#525254',
            'fontWeight': 'bold',
            'textAlign': 'left'
        },
        style_cell={
            'backgroundColor': '#AEA7A3',
            'textAlign': 'left',
            'padding': '8px',
            'font-family': 'Arial'
        }
    )
