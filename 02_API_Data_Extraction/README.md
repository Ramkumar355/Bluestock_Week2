# REST API & JSON Data Extraction

## Objective

This assignment demonstrates how to retrieve data from a public REST API, inspect the JSON response, convert the data into a Pandas DataFrame and CSV file, and perform basic data analysis and visualization.

## API Used

Frankfurter API

Website:
https://frankfurter.dev/

The API provides foreign exchange reference rates.

## HTTP Method

The project uses the HTTP GET method because we are retrieving data from the API.

## Query Parameters

The request uses:

- `base` — EUR
- `quotes` — USD and GBP
- `from` — starting date for the time-series data

## API Request Flow

API Endpoint
→ GET Request
→ JSON Response
→ Python
→ Pandas DataFrame
→ CSV
→ Analysis
→ Visualization

## JSON Response

The API returns structured JSON data containing fields such as:

- date
- base
- quote
- rate

The JSON response was inspected using Python before converting it into a DataFrame.

## Authentication

The Frankfurter API used in this assignment does not require an API key or authentication for the requested public data.

## Data Processing

The JSON response was converted into a Pandas DataFrame and exported to:

`exchange_rates.csv`

## Analysis

Basic analysis was performed by calculating:

- Minimum exchange rate
- Maximum exchange rate
- Average exchange rate
- Missing values

The data was also visualized using line charts to observe exchange-rate movement over time.

## Output Files

- `api_data_extraction.py` — Python implementation
- `exchange_rates.csv` — extracted API data
- `EUR_to_USD_exchange_rate.png` — USD visualization
- `EUR_to_GBP_exchange_rate.png` — GBP visualization

## Conclusion

This assignment demonstrates a basic data pipeline from a REST API to structured data suitable for analysis. The extracted exchange-rate data was successfully converted from JSON to CSV and visualized using Python.