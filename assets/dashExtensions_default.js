window.dashExtensions = Object.assign({}, window.dashExtensions, {
    default: {
        function0: function(feature, layer) {
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
                layer.bindTooltip(content, {
                    sticky: true
                });
            }
        }

    }
});