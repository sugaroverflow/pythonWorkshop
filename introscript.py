import urllib2
import json
from keys import WAPI_KEY

urlstring = 'http://api.wunderground.com/api/' + WAPI_KEY + '/geolookup/conditions/q/IA/Cedar_Rapids.json'

print WAPI_KEY

f = urllib2.urlopen(urlstring)
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['temp_f']

print "Current temperature in %s is: %s" % (location, temp_f)

f.close()
