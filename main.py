import pandas as pd
import numpy as np
import plotly.graph_objs as go
import ipywidgets as widgets
from IPython.display import display, clear_output

# Function to read stock data from CSV file and return a DataFrame
def read_stock_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Read main source file to get the list of companies and their stock data file paths
main_source_file = '10_Companies_details.csv'
main_data = pd.read_csv(main_source_file)

# Extract data for visualization
companies = main_data['Stock_Symbol']
market_caps = main_data['MarketCaps(Billions)']
trailing_pe = main_data['TrailingPE']
enterprise_value = main_data['EnterpriseValue(Billions)']

# Create a dictionary to store all stock dataframes
stock_data = {}
for index, row in main_data.iterrows():
    stock_symbol = row['Stock_Symbol']
    company_name = row['Company_Name']
    file_path = f'./{stock_symbol}_STOCKS_DATA.csv'
    stock_data[company_name] = read_stock_data(file_path)

# Initialize the figure
fig = go.Figure()

# Define checkbox widget
checkbox_options = [(company, True) for company in stock_data.keys()]
checkbox = widgets.Checkbox(options=checkbox_options, description='Select Companies:')

# Function to update the plot based on the selected companies
def update_plot(selected_companies):
    fig.data = []  # Clear existing traces
    for company, df in stock_data.items():
        if company in selected_companies:
            hover_template = f'<b>{company}</b><br>' + \
                             'Date: %{x}<br>' + \
                             'Open: %{customdata[0]:.2f}<br>' + \
                             'High: %{customdata[1]:.2f}<br>' + \
                             'Low: %{customdata[2]:.2f}<br>' + \
                             'Close: %{y:.2f}<br>' + \
                             'Volume: %{customdata[3]:,}<extra></extra>'
            fig.add_trace(go.Scatter(x=df['Date'],
                                     y=df['Close'],
                                     mode='lines',
                                     name=f'{company} Close',
                                     customdata=df[['Open', 'High', 'Low', 'Volume']],
                                     hovertemplate=hover_template))
            fig.update_traces(visible=True)
        else:
            fig.add_trace(go.Scatter(x=df['Date'],
                                     y=df['Close'],
                                     mode='lines',
                                     name=f'{company} Close',
                                     customdata=df[['Open', 'High', 'Low', 'Volume']],
                                     hovertemplate=hover_template,
                                     visible='legendonly'))
            fig.update_traces(visible=False)
    fig.update_layout(title='Stock Close Prices',
                      xaxis_title='Date',
                      yaxis_title='Close Price',
                      template='plotly_white')

# Define event handler for checkbox change
def on_checkbox_change(change):
    selected_companies = [option for option, value in change.new if value]
    with output:
        clear_output(wait=True)
        update_plot(selected_companies)
        fig.show()

# Attach event handler to checkbox
checkbox.observe(on_checkbox_change, names='value')

# Display checkbox widget and initial plot
output = widgets.Output()
display(widgets.VBox([checkbox, output]))

# Initial plot display
update_plot([company for company, _ in checkbox_options])
with output:
    fig.show()
