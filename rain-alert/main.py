import requests
import os
from twilio.rest import Client

# Accesses an api key hidden in the terminal's environment.
# Hide an api key by typing in the terminal export KEY_NAME=apiKey
api_key = os.environ.get("OWM_API_KEY")
weather_params = {
    "lat": 34.082729,
    "lon": -117.931480,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # Sends a message from my twilio account's phone number.
    message = client.messages \
        .create(
            body="It's going to rain! Bring an umbrella ☔",
            from_='+18449754123',
            to='+19092132807'
        )
    print(message.sid)
else:
    message = client.messages \
        .create(
            body="It's not going to rain! Go for a hike 🌳",
            from_='+18449754123',
            to='+19092132807'
        )
    print(message.sid)