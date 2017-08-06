import urllib.parse
import urllib.request
import json

# COMPILE QUERY
# ... See Yahoo Weather API Docs!
print("\n")

zipcode = input("Please enter your zipcode: ")
zipcode = str(zipcode)

baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text=" + zipcode +")"
yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"

# ISSUE REQUEST

response = urllib.request.urlopen(yql_url).read()

# PARSE RESPONSE
raw_response = json.loads(response)
results = raw_response["query"]["results"]["channel"]
weather = results["item"]

# PRINT STATEMENTS TO SEE DATA
#print(results)
#print(weather)

#SETTING UP COMMONLY USED ITEMS
conditions = (weather["condition"])
forecast = (weather["forecast"])

# CLOTHING RECOMMENDATIONS
temp = conditions['temp']
temp = int(temp)

def clothingreco():
    print("\n")
    print("-------------------------")
    print("\n")
    print("CLOTHING RECOMMENDATION:")
    print("\n")

    if temp<0:
        print("Considering it is",temp,"degrees outside, it's too cold. Stay inside!")
    elif temp<51:
        print("Considering it is",temp,"degrees outside, I recommend wearing a heavy coat!")
    elif temp<65:
        print("Considering it is",temp,"degrees outside, I recommend wearing a light coat.")
    elif temp<71:
        print("It is",temp,"degrees outside. Warm enough to wear a t-shirt!")
    elif temp<96:
        print("It is",temp,"degrees outside. Warm enough to wear a t-shirt and shorts!")
    elif temp>95:
        print("It is",temp,"degrees outside. Too HOT! Stay inside!!")
    print("\n")
    print("-------------------------")

# ADDING SOME FUN FUNCTIONALITY WITH PICTURES FOR A FEW POSSIBLE CONDITIONS (NOT ALL CONDITIONS AS THE LIST OF POSSIBILITIES IS PROHIBITIVE TO FIND PICTURES FOR)

def funwithweather():
    if conditions["text"] in {"Sunny","Mostly Sunny"}:
## credit to http://www.ascii-art.de/ascii/s/sun.txt Philip Kaulfuss
        print("""
                  .     :     .
            .  :    |    :  .
             .  |   |   |  ,
              \  |     |  /
          .     ,-'''''`-.     .
            "- /  __ __  \ -"
              |==|  I  |==|
        - --- | _`--^--'_ | --- -
              |'`.     ,'`|
            _- \  "---"  / -_
          .     `-.___,-'     .
              /  |     |  |
            .'  |   |   |  `.
               :    |    :
              .     :     .
             """)

## Credit to http://www.ascii-art.de/ascii/my/small3.shtml
    elif conditions["text"] in {"Partly Cloudy", "Mostly Cloudy", "Cloudy"}:
        print("""

            .               /
      \       I
                  /
        \  ,g88R_
          d888(`  ).                   _
 -  --==  888(     ).=--           .-(`  )`.
)         Y8P(       '`.          :(   .    )
        .+(`(      .   )     .--  `.  (    ) )
       ((    (..__.:'-'   .=(   )   ` _`  ) )
`.     `(       ) )       (   .  )     (   )  ._
  )      ` __.:'   )     (   (   ))     `-'.+(`  )
)  )  ( )       --'       `- __.'         :(      ))
.-'  (_.'          .')                    `(    )  ))
                  (_  )                     ` __.:'
                  """)

    elif conditions["text"] in {"Showers", "Thunderstorms", "Scattered Thunderstorms", "Scattered Showers", "Rain"}:
## Credit to Keith R. Fulton | keith.fulton@chinalake.navy.mil
## http://www.ascii-art.de/ascii/pqr/rain.txt

        print("""
       _
     _( )_          _
   _(     )_      _( )_
  (_________)   _(     )_
    \  \  \    (_________)
      \  \       \  \  \
                   \  \

""")


# PRINT CURRENT WEATHER CONDITIONS
def currentweather():
    print("\n")
    print(weather["title"])
    print("Latitude: ", weather["lat"])
    print("Longitude: ", weather["long"])
    print("\n")
    print("Currently it is",conditions["text"],"and",conditions['temp'],"degrees outside!")
    print("\n")

currentweather()

funwithweather()

clothingreco()

# PRINT WEATHER FORECAST
def weatherforecast():
    print("\n")
    print("10 DAY FORECAST:")
    print("\n")
    for d in forecast:
        print("The forecast for", d["day"], d["date"], "is", d["text"], "with a high of", d["high"], "and a low of", d["low"])
    print("\n")

weatherforecast()
