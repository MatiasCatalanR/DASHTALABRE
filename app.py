import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Crear una instancia de la aplicación Dash
app = dash.Dash(__name__)

# Datos de ejemplo para el gráfico
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# Crear un gráfico de barras
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Definir el layout de la aplicación
app.layout = html.Div(children=[
    html.H1(children='Prueba TICA'),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
