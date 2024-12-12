
Stock Data Visualization with Plotly and ipywidgets.

This Python script provides functionality to visualize stock data using Plotly for interactive plots and ipywidgets for interactive checkboxes. It enables users to select multiple companies and view their stock closing prices over time.

Requirements

- Python 3.x
- Pandas
- Plotly
- ipywidgets

Installation

To install the required libraries, run the following command:

pip install pandas plotly ipywidgets

Usage

1. Prepare Data Files:

   Ensure that you have the necessary CSV files containing stock data. The main source file (`10_Companies_details.csv`) should contain information about companies including their stock symbols, market caps, trailing P/E ratios, and enterprise values. Each company's stock data should be stored in separate CSV files named `<Stock_Symbol>_STOCKS_DATA.csv`.

2. Run the Script:

   Execute the Python script `main.py` in your preferred environment.

3. Interact with Widgets:

   - Upon running the script, a checkbox widget will appear with the names of available companies.
   - Select the company names you want to visualize.
   - The plot will dynamically update to display the closing prices of the selected companies over time.

Functionality

- The script reads stock data from CSV files and creates a DataFrame for each company.
- It provides an interactive checkbox widget allowing users to select multiple companies for visualization.
- The plot displays the closing prices of selected companies over time.
- Users can hover over data points to view detailed information including date, opening price, high price, low price, closing price, and volume.

File Structure

- `main.py`: The main Python script for data visualization.
- `10_Companies_details.csv`: The main source file containing details of companies.
- `<Stock_Symbol>_STOCKS_DATA.csv`: CSV files containing stock data for each company.

Credits

- This script was created by Shanmukha Sree Veda Tippavajhala.
- For any issues or suggestions, please contact Shanmukha.Tippavajhala@student.ufv.ca


