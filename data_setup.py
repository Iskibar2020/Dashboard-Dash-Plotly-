import pandas as pd
import json
from shapely.geometry import shape

# Load GeoJSON
with open("world_boundaries.geojson", "r", encoding='utf-8') as f:
    gj = json.load(f)

# Build dataframe including centroid coordinates
records = []
for feat in gj.get("features", []):
    props = feat.get("properties", {}).copy()
    try:
        geom = shape(feat.get("geometry", {}))
        centroid = geom.centroid
        props["latitude"] = centroid.y
        props["longitude"] = centroid.x
    except Exception:
        props["latitude"] = None
        props["longitude"] = None
    records.append(props)

df = pd.DataFrame.from_records(records)

# Ensure numeric columns
for col in ["pop_est", "gdp_md_est"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Global min/max population for slider defaults
if "pop_est" in df.columns and not df["pop_est"].dropna().empty:
    pop_vals = df["pop_est"].dropna()
    pop_vals = pop_vals[pop_vals > 0]
    GLOBAL_MIN_POP = int(pop_vals.min())
    GLOBAL_MAX_POP = int(pop_vals.max())
else:
    GLOBAL_MIN_POP = 0
    GLOBAL_MAX_POP = 0

# Continent dropdown options
tmp = df.get("continent", pd.Series(dtype=str)).dropna().unique()
continent_options = [{"label": c, "value": c} for c in sorted(tmp)]
