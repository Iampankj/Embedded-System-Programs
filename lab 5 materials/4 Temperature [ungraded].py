from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

temp = sense.get_temperature()
print(temp)
temp_pressure = sense.get_temperature_from_pressure()
print(temp_pressure)