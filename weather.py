import os
import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO
from dotenv import load_dotenv

from SCWindow import SCWindow, runIfLocal

class weatherWindow(SCWindow):
    def __init__(self, parent=None, title='Stellar Client Weather', geometry="1000x600"):
        super().__init__(parent, title, geometry)
    
    def createCustomWidgets(self, mainFrame):
        self.weatherFrame = tk.Frame(mainFrame, bg="white")
        self.weatherFrame.pack(fill='x', pady=(0, 10))

        self.updateButton = tk.Button(
            self.weatherFrame,
            text='Update Weather data',
            font=(
                'Castellar',
                16
            ),
            bg='white',
            fg='black',
            command=self.update
        )
        self.updateButton.pack(pady=(0, 10))

        self.weatherImage = ImageTk.PhotoImage(self.getWeatherIcon())
        self.weatherImageLabel = tk.Label(
            self.weatherFrame,
            image=self.weatherImage,
            bg='white'
        )
        self.weatherImageLabel.pack(pady=(0, 10))
        self.weatherImageLabel.image = self.weatherImage

        self.temperatureBox = tk.Text(
            self.weatherFrame,
            font=(
                'Arial',
                16
            ),
            bg='white',
            fg='black',
            state='disabled'
        )
        self.temperatureBox.pack(pady=(0, 10))
    
    def getLocationInfo(self): #TODO: same issue as below
        # Get IP address
        ip_response = requests.get('https://api.ipify.org?format=json').json()
        ip_address = ip_response['ip']

        # Get location from IP address
        location_response = requests.get(f'http://ip-api.com/json/{ip_address}').json()

        result = {
            "City": location_response['city'],
            "State_Code": location_response['region'],
            "Country_Code": location_response['countryCode']
        }
        # print(f"Latitude: {location_response['lat']}")
        # print(f"Longitude: {location_response['lon']}")
        return result
    
    def getWeatherInfo(self): #TODO: Theres a lot of risks here, work on later
        location = self.getLocationInfo()

        load_dotenv()

        WEATHER_KEY = os.getenv("WEATHER_KEY")

        if WEATHER_KEY == None:
            raise LookupError("Weather key is None")

        geoUrl = f"http://api.openweathermap.org/geo/1.0/direct?q={location['City'].strip().replace(' ', '-')},{location['State_Code'].strip().replace(' ', '-')},{location['Country_Code'].strip().replace(' ', '-')}&appid={WEATHER_KEY}"

        latLon = requests.get(geoUrl).json()
        if latLon == None:
            raise ValueError("Latitude-Longitude get call is None")

        url = f"https://api.openweathermap.org/data/2.5/weather?lat={latLon[0]['lat']}&lon={latLon[0]['lon']}&appid={WEATHER_KEY}&units=metric"

        response = requests.get(url).json()
        if response == None:
            raise ValueError("Weather get call is None")

        dt = {
            'Location': response['name'],
            'Temperature': response['main']['temp'],
            'Conditions': response['weather'][0]['description'],
            'High/Low': (str(response['main']['temp_max'])+'°', str(response['main']['temp_min'])+'°'),
            'Wind': response['wind'],
            'Weather-Icon': response['weather'][0]['icon']
        }

        return dt
    
    def getWeatherIcon(self):
        imageName = self.getWeatherInfo()['Weather-Icon']
        url = f'https://openweathermap.org/img/wn/{imageName}@2x.png'
        imgResponse = requests.get(url) 
        if imgResponse == None:
            raise ValueError("Icon get call is None")
        imgResponse.raise_for_status()
        imgBinary = imgResponse.content
        imgDT = BytesIO(imgBinary)
        image = Image.open(imgDT)
        return image

    def update(self):
        try:
            weather = self.getWeatherInfo()
        except Exception as e:
            self.temperatureBox.config(state="normal")
            self.temperatureBox.delete("1.0", tk.END)
            self.temperatureBox.insert(tk.END, f"Error in weather fetching: {e}")

        self.temperatureBox.config(state='normal')
        self.temperatureBox.delete("1.0", tk.END)
        self.temperatureBox.insert(tk.END, f"Location: {weather['Location']}\n")
        self.temperatureBox.insert(tk.END, f"Temperature: {weather['Temperature']}°C\n")
        self.temperatureBox.insert(tk.END, f"Conditions: {weather['Conditions'].capitalize()}\n")
        tempHighLow = str(weather['High/Low']).strip('(').strip(')').replace("'", "")
        self.temperatureBox.insert(tk.END, f"Temperature High/Low: {tempHighLow}\n")
        wind = weather['Wind']
        speed = wind.get('speed', 'N/A')
        deg = wind.get('deg', 'N/A')
        gust = wind.get('gust', None)
        speed_str = f"{speed} m/s" if speed != 'N/A' else 'N/A'
        deg_str = f"{deg}°" if deg != 'N/A' else 'N/A'
        gust_str = f"{gust} m/s" if gust is not None else 'N/A'
        self.temperatureBox.insert(tk.END, f"Wind: Speed: {speed_str}, Degrees: {deg_str}, Gust: {gust_str}\n")
        self.temperatureBox.config(state='disabled')
    
    def onStart(self):
        self.update() # TODO: make threaded maybe, need discussion


runIfLocal(weatherWindow, __name__)