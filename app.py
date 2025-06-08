from dash import Dash
import layouts
import callbacks
import plotly.io as pio
import os

def main():
    # Load template.html for index_string
    with open('assets/template.html', 'r', encoding='utf-8') as f:
        template_string = f.read()

    app = Dash(__name__, external_stylesheets=[], index_string=template_string)

    # Load layout & callbacks
    layouts.init_layout(app)
    callbacks.register_callbacks(app)

    return app

if __name__ == '__main__':
    app = main()  # ← THIS FIXES THE ERROR
    port = int(os.environ.get('PORT', 8050))
    app.run(debug=False, host='0.0.0.0', port=port)
