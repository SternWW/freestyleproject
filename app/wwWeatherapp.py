import urllib.parse
import urllib.request
import json

# COMPILE QUERY
# ... See Yahoo Weather API Docs!
print("\n")

zipcode = input("Please enter your zipcode: ")
zipcode = str(zipcode)

#while True:



baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text=" + zipcode +")"
yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"

# ISSUE REQUEST

response = urllib.request.urlopen(yql_url).read()

# PARSE RESPONSE

raw_response = json.loads(response)
results = raw_response["query"]["results"]["channel"]
weather = results["item"]

#print(results)
#print(weather)
print("\n")
print(weather["title"])
print("Latitude: ", weather["lat"])
print("Longitude: ", weather["long"])

conditions = (weather["condition"])
#print(conditions)

#def what_to_wear():
#    if conditions["text"]
#Options = Thunderstorms, partly cloudy, rain, mostly cloudy

print("Currently it is ",conditions["text"],"and",conditions['temp'],"degrees outside!")

forecast = (weather["forecast"])

#print("\n")
#print(weather)
#print("\n")
#print(conditions)
print("\n")
#print(forecast)
#forecast = dict(forecast)
#for key, value in forecast.items() :
#    print (key, value)

for d in forecast:
    print("The forecast for", d["day"], d["date"], "is", d["text"], "with a high of", d["high"], "and a low of", d["low"])

#print(forecast["day"])

#for day in forecast:

#print(forecast[int("day")])


#item = 'temp'

#for key in weather.keys():
#    if item in weather["condition"]:
#        print(key)
