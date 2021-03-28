import requests

API_KEY = input("API-key: ")
API_URL = "https://api.solcast.com.au/weather_sites/b185-4967-4cd7-c7b7/forecasts?format=json&api_key=" + API_KEY

try:
    resp = requests.get(API_URL)
    if resp.status_code != 200:     # This means something went wrong
        raise requests.ConnectionError('GET /https://api.solcast.com.au/weather_sites/b185-4967-4cd7-c7b7/estimated_actuals?format=json/ {}'.format(resp.status_code))
    print(resp.json())
    
except Exception as e:
    print("Could not connect to the API")
    print(str(e))
