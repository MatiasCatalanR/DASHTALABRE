import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

app = dash.Dash(__name__)
server = app.server

# Datos para el gráfico
data = px.data.iris()

# Crear el gráfico utilizando Plotly Express
fig = px.scatter(data, x="sepal_width", y="sepal_length", color="species")

app.layout = html.Div(
    children=[
        html.H1("Prueba N°2 Migración desde Streamlit a Dash"),
        html.P("TICA."),
        dcc.Graph(figure=fig)  # Agregar el gráfico a la página utilizando el componente dcc.Graph
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
