import requests
2
api_key = 'api_key_goes_here'  # replace with your actual API key
user_input = input("ENTER THE CITY NAME: ")
# this is the exact format required
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")
# units=metric gives temp in celcius and unit=imperials gives temp in celcius and also [0] is used to get the first result in dictionary or data.
# we didnt write it for temp bcz temp bcz in most api,temp isnt stored inside the list

weather = weather_data.json()['weather'][0]['main']
# round()...gives a more understandable temp bcz otherwise it would give in decimals
temp = round(weather_data.json()['main']['temp'])
print(weather)
print(temp)

# this is another set of a weather app
api_key = '12357e09a8a15cc75bf9165011b0cd3d'
user_input = input("ENTER THE CITY NAME: ")
weather = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")
data = weather.json()
print("Weather: ", data['weather'][0]['main'])
print("Temperature: ", round(data['main']['temp']), "celsius")
print("Humidity: ", data['main']['humidity'], "%")
print("Wind speed: ", data['wind']['speed'], "m/s")
