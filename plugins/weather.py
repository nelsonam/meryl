from errbot import BotPlugin, botcmd
import json
import requests

class Weather(BotPlugin):
    @botcmd
    def weather(self, msg, args):
        print args
        location = args # city
        
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + str(location))
        response = r.json()
        
        temp_K = response['main']['temp']
        temp_C = temp_K - 273.15
        temp_F = temp_K * (9/5.0) - 459.67

        return 'It looks like ' + str(temp_F) + u"\u2109" + '/' + str(temp_C) + u"\u2103" + ' and ' + response['weather'][0]['description'] + ' there in ' + response['name']

    
