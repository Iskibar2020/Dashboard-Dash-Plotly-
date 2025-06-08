from dash import Dash
import layouts
import callbacks
import plotly.io as pio


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
    main().run_server(debug=True)
