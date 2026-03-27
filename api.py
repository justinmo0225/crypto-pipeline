import requests

# API: "https://api.coingecko.com/api/v3/coins/bitcoin" outputs price of BTC at accessed timestamp

def getBIT():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin"
    response = requests.get(url)
    data = response.json()

    if "market_data" in data:
        return data["market_data"]["current_price"]["usd"]
    else:
        print("API error:", data)
        return None