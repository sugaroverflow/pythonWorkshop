#!/usr/bin/env python

# import modules used here
import sys
import json
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlopen
from keys import WAPI_KEY

def get_current_conditions(city):
  """
  Returns the current conditions of a city in Canada.
  """
  response = urllib2.urlopen('http://api.wunderground.com/api/' + WAPI_KEY + '/conditions/q/canada/' + city + '.json')
  data = json.load(response)

  fname = city + '-current-conditions'
  with open(fname + '.json', 'w') as outfile:
    json.dump(data, outfile)

  return data

def get_current_temperature(city):
  json_data = get_current_conditions(city)
  temp_c = json_data['current_observation']['temp_c']
  print ("Current temperature in %s is: %s" % (city, temp_c))

def get_current_temp_from_file(city):
  fname = 'data-' + city
  with open(fname + '.json') as json_data:
    data = json.load(json_data)
  temp_c = data['current_observation']['temp_c']
  fl_temp_c = data['current_observation']['feelslike_c']
  print ("Current temperature in %s is: %s" % (city, temp_c))
  print ("Feels like: %s" % (fl_temp_c))

def get_ten_day_forecast(city):
  """
  Returns the 10 day forecast of a city in Canada.
  """
  response = urllib2.urlopen('http://api.wunderground.com/api/' + WAPI_KEY + '/forecast10day/q/canada/' + city + '.json')
  data = json.load(response)

  fname =  city + 'ten-day-forecast'
  with open(fname + '.json', 'w') as outfile:
    json.dump(data, outfile)

  for day in data['forecast']['simpleforecast']['forecastday']:
    print (day['date']['weekday'] + ":")
    print ("Conditions: ", day['conditions'])
    print ("High: ", day['high']['celsius'] + "C", "Low: ", day['low']['celsius'] + "C", '')


  return data


# Gather our code in a main() function
def main():
  data = get_ten_day_forecast('London')
  # get_current_temperature('London')
  # get_current_temp_from_file('London')


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
