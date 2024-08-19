import requests

class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_Data()

    def get_Data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=remove_this_text_and_add_your_API")
        except:
            print("No Internet available right now. Try again.")
            return

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]
        self.name = self.response_json["name"]

    def temp_print(self):
            print(f"In {self.name} it is currently {self.temp}° C")
            print(f"Today's High: {self.temp_max}° C")
            print(f"Today's Low: {self.temp_min}° C")


my_city = City("Tokyo", 35.6764, 139.6500) # Name showing as Horinouchi in Json files. 
my_city.temp_print()

home_city = City("Gurgaon", 28.4595, 77.0266)
home_city.temp_print()
