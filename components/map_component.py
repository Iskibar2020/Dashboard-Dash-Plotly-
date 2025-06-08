
import dash_leaflet as dl
from dash_extensions.javascript import assign
import data_setup

# JS tooltip function for each feature
tooltip_js = assign("""
function(feature, layer){
  if (feature.properties) {
    const p = feature.properties;
    const content = `
      <div>
        <strong>${p.name}</strong><br/>
        Postal Code: ${p.postal.toLocaleString()}<br/>
        Formal Name: ${p.formal_en.toLocaleString()}<br/>
        Population: ${p.pop_est.toLocaleString()}<br/>
        GDP (M USD): ${p.gdp_md_est.toLocaleString()}<br/>
        Last Census: ${p.lastcensus.toLocaleString()}<br/>
        Economy: ${p.economy.toLocaleString()}<br/>
        Income Level: ${p.income_grp.toLocaleString()}<br/>
        Continent: ${p.continent.toLocaleString()}<br/>
        Subregion: ${p.subregion.toLocaleString()}<br/>
        Area: ${p.Shape_Area.toLocaleString()}
      </div>
    `;
    layer.bindTooltip(content, {sticky: true});
  }
}
""")

def map_ui():
    return dl.Map(
        id="boundary-map",
        center=[0, 0],
        zoom=1,
        style={"width": "100%", "height": "620px"},
        children=[
            dl.LayersControl(
                [
                    # Base tile layers (user can switch between these)
                    dl.BaseLayer(
                        dl.TileLayer(
                            url="http://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
                            attribution="&copy; Google Satellite",
                            subdomains=["mt0", "mt1", "mt2", "mt3"],
                        ),
                        name="Google Satellite",
                    ),
                    dl.BaseLayer(
                        dl.TileLayer(
                            url="http://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
                            attribution="&copy; Google Hybrid",
                            subdomains=["mt0", "mt1", "mt2", "mt3"],
                        ),
                        name="Google Hybrid",
                        
                    ),
                    dl.BaseLayer(dl.TileLayer(url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"), name="OpenStreetMap",checked=True),
                    dl.BaseLayer(dl.TileLayer(url="https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png"), name="OpenTopoMap"),
                    

                    # Overlay layers (can toggle on/off)
                    dl.Overlay(
                        dl.GeoJSON(
                            id="geojson",
                            data=data_setup.gj,
                            style={
                                "color": "#2f302b",
                                "weight": 2,
                                "fillColor": "#525453",
                                "fillOpacity": 0.5,
                            },
                            hoverStyle={"weight": 4, "color": "#2c3c4c", "dashArray": ""},
                            onEachFeature=tooltip_js,
                        ),
                        name="Country Boundaries",
                        checked=True,
                    ),
                ]
            )
        ]
    )
