import tkinter as tk;
import datetime;
from tkinter import ttk;
import requests


def getData():
    city = cityName.get()
    apiURL = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
    response = requests.get(apiURL, headers={"APIKEY"})
    if response.status_code == requests.codes.ok:
        data = response.json()
        messageInfo.set("Data of {}".format(city))
        temperature.set("Temperature: {}°C".format(data["temp"]))
        max_temp.set("Max Temperature: {}°C".format(data["max_temp"]))
        windSpeed.set("Wind Speed: {}m/s".format(data["wind_speed"]))
        humidity.set("Humidity: {}%".format(data["humidity"]))
        clouds.set("Clouds {}".format(data["cloud_pct"]))
        riseTime = datetime.datetime.fromtimestamp(data["sunrise"])
        setTime = datetime.datetime.fromtimestamp(data["sunset"])
        sunrise.set("Sun Rise: {}".format(riseTime))
        sunset.set("Sun Set: {}".format(setTime))
        
    else:
        print("Error: ", response.status_code, response.text)
        messageInfo.set("City not found") 
    

root = tk.Tk()
root.title("My Weather")
root.configure(background="black")
root.geometry("300x400")

heading = ttk.Label(text="My Weather App", font=("Calibri", 20), foreground="white", background="black")
heading.grid(row=0, column=2, pady=10, padx=60)

cityName = ttk.Entry(foreground="blue", font=("Verdana", 12))
cityName.grid(row=1, column=1, columnspan=2, padx=50, pady=10)

searchBtn = ttk.Button(text="Get Weather Info", command=getData )    
searchBtn.grid(row=2, column=2, padx=50, pady=2)

messageInfo = tk.StringVar(value="No Data Available!")
temperature = tk.StringVar()
max_temp  = tk.StringVar()
windSpeed  = tk.StringVar()
sunrise = tk.StringVar()
sunset = tk.StringVar()
humidity = tk.StringVar()
clouds = tk.StringVar()

message = ttk.Label(root, textvariable=messageInfo, foreground="white", background="black", font=10) 
message.grid(row=4, column=2, padx=50, pady=30)


temperature_label = ttk.Label(textvariable=temperature, foreground="white", background="black", font=8)
temperature_label.grid(row=5, column=2, padx=50, pady=2)

maxtemp_label = ttk.Label(textvariable=max_temp, foreground="white", background="black", font=8)
maxtemp_label.grid(row=6, column=2, padx=50, pady=2)

windspeed_label = ttk.Label(textvariable=windSpeed, foreground="white", background="black", font=8)
windspeed_label.grid(row=7, column=2, padx=50, pady=2)

sunrise_label = ttk.Label(textvariable=sunrise, foreground="white", background="black", font=8)
sunrise_label.grid(row=8, column=2, padx=50, pady=2)

sunset_label = ttk.Label(textvariable=sunset, foreground="white", background="black", font=8)
sunset_label.grid(row=9, column=2, padx=50, pady=2)

humidity_label = ttk.Label(textvariable=humidity, foreground="white", background="black", font=8)
humidity_label.grid(row=10, column=2, padx=50, pady=2)

clouds_label = ttk.Label(textvariable=clouds, foreground="white", background="black", font=8)
clouds_label.grid(row=11, column=2, padx=50, pady=2)

clouds_label = ttk.Label(text="GrowIntern Python Developer - Sarfaraz", foreground="springgreen", background="black", font=5)
clouds_label.grid(row=11, column=2, padx=10, pady=2)


root.mainloop()