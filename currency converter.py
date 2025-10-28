import requests
# api_keys → not needed here, since exchangerate.host doesn’t require an API key.

currency_codes = {
    "USD": "United States Dollar",
    "EUR": "Euro",
    "GBP": "British Pound Sterling",
    "JPY": "Japanese Yen",
    "CHF": "Swiss Franc",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "NZD": "New Zealand Dollar",
    "CNY": "Chinese Yuan Renminbi",
    "INR": "Indian Rupee",
    "AED": "United Arab Emirates Dirham",
    "SAR": "Saudi Riyal",
    "SGD": "Singapore Dollar",
    "HKD": "Hong Kong Dollar",
    "THB": "Thai Baht",
    "MYR": "Malaysian Ringgit",
    "ZAR": "South African Rand",
    "BRL": "Brazilian Real",
    "MXN": "Mexican Peso",
    "KRW": "South Korean Won"
}

from_currency = input("ENTER THE CURRENCY YOU HAVE: ").upper()
to_currency = input("ENTER THE CURRENCY TO YOU WANT YOUR RESULTS IN: ").upper()
amount = float(input("ENTER THE AMOUNT: "))

url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"

response = requests.get(url)
data = response.json()


print(f"{'amount'} {from_currency}=data{['result']}{to_currency}")
