import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load and preprocess the data
df = pd.read_csv("output.csv")
df['sales'] = df['sales'].replace('[\$,]', '', regex=True).astype(float)
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Create the Dash app
app = dash.Dash(__name__)

# Create line chart
fig = px.line(df, x='date', y='sales', title='Sales Over Time')

# App layout
app.layout = html.Div(children=[
    html.H1('Sales Line Chart'),
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)