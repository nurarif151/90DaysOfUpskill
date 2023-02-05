import requests

def convert_currency(amount, from_currency, to_currency):
    API_KEY = "BqTcsveHc4Pt3w7Z43Dn3HETbTPCkLeP"
    API_URL = f"http://data.fixer.io/api/latest?access_key={API_KEY}&symbols={from_currency},{to_currency}"
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        if "rates" in data:
            from_rate = data["rates"][from_currency]
            to_rate = data["rates"][to_currency]
            result = amount * (to_rate / from_rate)
            return result
        else:
            return None
    else:
        return None

print(convert_currency(100, "USD", "EUR"))
