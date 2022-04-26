class CurrentWeather:
    weather_data = {'Toronto':['13','partly sunny','8 km/h NW'],
                    'Montreal':['16','mostly sunny','22 km/h W'],
                    'Vancouver':['18','thunder showers','10 km/h NE'],
                    'New York':['17','mostly cloudy','5 km/h SE'],
                    'Los Angeles':['28','sunny','4 km/h SW'],
                    'London':['12','mostly cloudy','8 km/h NW'],
                    'Mumbai':['33','humid and foggy','2 km/h S'] }
    def __init__(self, city):
        self.city = city
    def get_temperature(self):
        return self.weather_data[self.city][0]
    def get_weather_conditions(self):
        return self.weather_data[self.city][1]
    def get_wind_speed(self):
        return self.weather_data[self.city][2]