import requests
import pandas as pd
url = "https://api.frankfurter.dev/v2/rates"

params = {
    "base": "EUR",
    "quotes": "USD,GBP",
    "from": "2026-01-01"
}
response = requests.get(url, params=params)
print("Status Code:", response.status_code)
data = response.json()
df = pd.DataFrame(data)
print("\nFirst 5 rows:")
print(df.head())
df.to_csv("exchange_rates.csv", index=False)
# Basic analysis
print("\nSummary Statistics:")
print(df.groupby("quote")["rate"].agg(["min", "max", "mean"]))

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())
print("\nCSV file created successfully!")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df["date"] = pd.to_datetime(df["date"])

for currency in df["quote"].unique():
    currency_data = df[df["quote"] == currency]

    plt.figure(figsize=(10, 5))
    plt.plot(currency_data["date"], currency_data["rate"])

    plt.title(f"EUR to {currency} Exchange Rate")
    plt.xlabel("Date")
    plt.ylabel("Exchange Rate")

    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"EUR_to_{currency}_exchange_rate.png", dpi=300)
plt.show()