#!/usr/bin/env python

# import modules used here
import sys
import json
import csv
import os
from urllib.request import urlopen
from keys import WAPI_KEY

def get_weather_json(city):
    """
    Gets the 10 day forecast of a city in Canada.
    And writes it to a CSV file.
    """
    response = urlopen('http://api.wunderground.com/api/' + WAPI_KEY + '/forecast10day/q/canada/' + city + '.json')
    data = json.load(response)

    with open('%s.csv' % city, 'w') as outfile:
      writer = csv.writer(outfile)
      writer.writerow(["Day", "Low Temp"])

      for day in data['forecast']['simpleforecast']['forecastday']:
        row = []
        row.append(str(day['date']['weekday']))
        row.append(day['low']['celsius'])
        writer.writerow(row)

# Gather our code in a main() function
def main():
  get_weather_json('London')

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
