import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load and preprocess the data
df = pd.read_csv("output.csv")
df['sales'] = df['sales'].replace('[\$,]', '', regex=True).astype(float)
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Create the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div(children=[
    html.H1('Sales Line Chart'),
    dcc.Graph(id='sales-line-chart'),
    html.Br(),
    html.Label('Select Region'),
    dcc.RadioItems(
        id='region-selector',
        options=[
            {'label': region.title(), 'value': region} for region in ['north', 'east', 'south', 'west', 'all']
        ],
        value='all',
        inline=True
    )
])

# Callback to update the chart
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-selector', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(filtered_df, x='date', y='sales', title=f'Sales Over Time - {selected_region.title()}')
    return fig

if __name__ == '__main__':
    app.run(debug=True)