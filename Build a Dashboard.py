import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    dcc.Dropdown(id='campaign-dropdown', options=[{'label': i, 'value': i} for i in merged_df['Campaign Name'].unique()], value='All Campaigns'),
    dcc.Graph(id='performance-graph')
])

@app.callback(
    Output('performance-graph', 'figure'),
    Input('campaign-dropdown', 'value'))
def update_graph(selected_campaign):
    if selected_campaign == 'All Campaigns':
        filtered_df = merged_df
    else:
        filtered_df = merged_df[merged_df['Campaign Name'] == selected_campaign]
    
    fig = px.bar(filtered_df, x='Campaign Name', y='Conversions', title='Conversions by Campaign')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
