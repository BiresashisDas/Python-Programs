# Author :- Biresashis Das

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["Day"])          # It will print the Day column from the weather.csv file
print(data["Temperature"])  # It will print the Temperature column from the weather.csv file
print(data["Weather"])      # It will print the Weather column from the weather.csv file



