from bs4 import BeautifulSoup as soup
import requests

# For Inputs
states = {
    "al": "Alabama",
    "ak": "Alaska",
    "az": "Arizona",
    "ar": "Arkansas",
    "ca": "California",
    "co": "Colorado",
    "ct": "Connecticut",
    "de": "Delaware",
    "dc": "District of Columbia",
    "fl": "Florida",
    "ga": "Georgia",
    "gu": "Guam",
    "hi": "Hawaii",
    "id": "Idaho",
    "il": "Illinois",
    "in": "Indiana",
    "ia": "Iowa",
    "ks": "Kansas",
    "ky": "Kentucky",
    "la": "Louisiana",
    "me": "Maine",
    "md": "Maryland",
    "ma": "Massachusetts",
    "mi": "Michigan",
    "mn": "Minnesota",
    "ms": "Mississippi",
    "mo": "Missouri",
    "mt": "Montana",
    "ne": "Nebraska",
    "nv": "Nevada",
    "nh": "New Hampshire",
    "nj": "New Jersey",
    "nm": "New Mexico",
    "ny": "New York",
    "nc": "North Carolina",
    "nd": "North Dakota",
    "mp": "Northern Mariana Islands",
    "oh": "Ohio",
    "ok": "Oklahoma",
    "or": "Oregon",
    "pa": "Pennsylvania",
    "pr": "Puerto Rico",
    "ri": "Rhode Island",
    "sc": "South Carolina",
    "sd": "South Dakota",
    "tn": "Tennessee",
    "tx": "Texas",
    "tt": "Trust Territories",
    "ut": "Utah",
    "vt": "Vermont",
    "va": "Virginia",
    "vi": "Virgin Islands",
    "wa": "Washington",
    "wv": "West Virginia",
    "wi": "Wisconsin",
    "wy": "Wyoming"
}
def state_abbrev(input):
    for key,value in states.items():
        if value.lower() == input.lower():
            return key
    return None

def city_fix(input):
    if " " in input:
            words = input.split()
            city = "-".join(words)
            return city.lower()
    else:
        return input.lower()
    return None

def get_coords(city, state):
    url = f'https://www.wunderground.com/weather/us/{state}/{city.lower()}'

    req = requests.get(url)
    web_page = req.content

    web = soup(web_page,'html.parser')

    name_box = web.find('span', class_ = 'subheading')
    name = name_box.text.split() 
    # print(name)

    for item in name:
        # print(item)
        if "°N" in item:
            lat = float(name[3])
        elif "°S" in item:
            lat = float(name[3])
            lat = lat * (-1)
        elif "°W" in item:
            long = float(name[5])
            long = long * (-1)
        elif "°E" in item:
            long = float(name[5])
    # print(lat)
    # print(long)

   
    return lat, long

# Using Webscraping
def condition_simple(city,state,type,class_,dict_name):
    url = f'https://www.wunderground.com/weather/us/{state}/{city.lower()}'
    req = requests.get(url)
    web_page = req.content
    web = soup(web_page,'html.parser')
    name_box = web.find(type, class_)
    name = name_box.text.split() 
    
    if dict_name == 'time':
        dict = {dict_name: name[1:8]}
    else: 
        dict = {dict_name: name}
    return dict

def info(condition, city, state):
    
    if condition == "coordinates":
        condition = get_coords(city,state)
    elif condition == "time":
        condition = condition_simple(city,state,'p','timestamp','time')
    elif condition == "high":
        condition = condition_simple(city,state,'span','hi','high')
    elif condition == "low":
        condition = condition_simple(city,state,'span','lo','low')
    elif condition == "temperature":
        next
        # condition = condition_simple(city,state,'div','cur-temp has-degs temp40 funits','temperature')
    elif condition == "feels like":
        condition = condition_simple(city,state,'span','temp','feels like')
    elif condition == "condition":
        condition = condition_simple(city,state,'div','condition-icon small-6 medium-12 columns','condition')
    elif condition == "humidity":
        condition = condition_simple(city,state,'span','test-false wu-unit wu-unit-humidity ng-star-inserted','humidity')
    elif condition == "gusts":
        condition = condition_simple(city,state,'span','test-false wu-unit wu-unit-speed ng-star-inserted','wind gusts')
    elif condition == "wind speed":
        condition = condition_simple(city,state,'header','wind-speed','wind speed')
    return condition

def complete(city,state):
    city_1 = city_fix(city)
    state_1 = state_abbrev(state)


    dict = {}
    coords = []
    time = []
    high = []
    low = []
    temp = []
    condition = []
    feels_like = []
    humidity = []
    gusts = []
    wind_speed = []

    coords = info("coordinates", city_1, state_1)
    time = info('time', city_1, state_1)
    high = info('high', city_1, state_1)
    low = info('low', city_1, state_1)
    temp = info('temperature', city_1, state_1)
    condition = info('condition', city_1, state_1)
    feels_like = info('feels like', city_1, state_1)
    humidity = info('humidity', city_1, state_1)
    gusts = info('gusts', city_1, state_1)
    wind_speed = info('wind speed', city_1, state_1)
    
    dict = [coords, time, high, low, temp, condition, feels_like, humidity, gusts, wind_speed]
    return dict








# API

import requests
import json




my_key = "cb89c37822875b5b47319c98f6cb1522"

# Function to get live stock data for a symbol
def get_weather(lat, lon, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data
    # if response.status_code == 200:
    #     data = response.json()
    #     return data
    # else:
    #     return None


coords = get_coords("portland","me")
weather = get_weather(coords[0],coords[1],my_key)

print(weather)

