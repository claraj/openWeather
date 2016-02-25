#Fetches weather from openweatherapi, extracts temp from json
    #not used at all in this application but I wrote this to practice fetching data from an API.
    def getWeather(self):

        #Example 2 - fetch JSON from openweathermap
        weatherurl = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk'
        #Make request, get response
        weatherResponse = urllib.request.urlopen(weatherurl)
        #Read response into JSON string

        wresponseJson = weatherResponse.read().decode('utf-8')
        #Reference http://stackoverflow.com/questions/23049767/parsing-http-response-in-python

        print(wresponseJson)
        #Load JSON string into JSON parser - now can be used in a dictionary-like way
        parsed_json = json.loads(wresponseJson)
        #Reference http://docs.python-guide.org/en/latest/scenarios/json/
        #What's the temp in London?

        tempInKelvin = parsed_json['main']['temp']
        tempInCelcius = int(tempInKelvin) - 273
        print(tempInCelcius)
