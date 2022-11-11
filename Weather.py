import requests
from datetime import datetime
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+"28ae06d918baf52c7af56ccfb24980d2"

api_link = requests.get(complete_api_link)
api_data = api_link.json()


if api_data['cod'] == '404':
    print("Invaild City: {},Please Check Your City Name".format(location))
else:
    #create variables to store and display data
    #temp_city = ((api_data['main']['temp']) - 273.15)
    tempcity = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    pressure = api_data['main']['pressure']
    min_temp = ((api_data['main']['temp_min']) - 273.15)
    max_temp = ((api_data['main']['temp_max']) - 273.15)
    feelslike = ((api_data['main']['feels_like']) - 273.15)
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print ("-------------------------------------------------------------")
    print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    print ("-------------------------------------------------------------")

    print ("Current temperature is: {:.2f} deg C".format(tempcity))
    print ("Current weather desc  :",weather_desc)
    print ("Current Humidity      :",hmdt, '%')
    print ("Current Pressure      :",pressure,"mbar")
    print ("Current wind speed    :",wind_spd ,'kmph')
    print ("Minimum temperature    :{:.2f} deg C".format(min_temp))
    print ("Maximum temperature    :{:.2f} deg C".format(max_temp))
    print ("Feels Like             :{:.2f} deg C".format(feelslike))
