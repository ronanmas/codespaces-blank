from bs4 import BeautifulSoup as soup
import requests

# Finding coordinates from city, state
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
    return input

def city_fix(input):
    if " " in input:
            words = input.split()
            city = "-".join(words)
            return city.lower()
    else:
        return input.lower()

def get_coords(city, state):
    url = f'https://www.wunderground.com/weather/us/{state}/{city.lower()}'

    req = requests.get(url)
    web_page = req.content

    web = soup(web_page,'html.parser')

    name_box = web.find('span', class_ = 'subheading')
    name = name_box.text.split() 

    for item in name:
        if "°N" in item:
            lat = float(name[3])
        elif "°S" in item:
            lat = float(name[3])
            lat = lat * (-1)
        elif "°W" in item:
            lon = float(name[5])
            lon = lon * (-1)
        elif "°E" in item:
            lon = float(name[5])
    return lat, lon

# Process Request
API_KEY = "cb89c37822875b5b47319c98f6cb1522"

def get_weather(city,state):
    city = city_fix(city)
    state = state_abbrev(state)
    lat, lon = get_coords(city, state)
    return get_weather_coords(lat, lon, API_KEY)
def get_weather_coords(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial"
    response = requests.get(url)
    data = response.json()
    TEMP_UNIT = " ˚F"
    WIND_UNIT = " mph"
    return {
        "temp": str(data["main"]["temp"])+TEMP_UNIT,
        "feels like": str(data["main"]["feels_like"])+TEMP_UNIT,
        "high": str(data["main"]["temp_max"])+TEMP_UNIT,
        "low": str(data["main"]["temp_min"])+TEMP_UNIT,
        "wind speed": str(data["wind"]["speed"])+WIND_UNIT,
        "condition": data["weather"][0]["main"].lower(),
        "humidity": data["main"]["humidity"]
    }
def parse_request(request):
    # in the future we'll parse the request using a cfg file and such, but right
    # now I just want the scaffolding in place so I'm doing it this way
    # This is the function I expect to change the most in finishing the implementation
    return {
        "city": request[0],
        "state": request[1],
        "feature": request[2]
    }

# Response
FULL_NAME = {
    "temp": "temperature",
    "feels like": "feels like",
    "high": "high for today",
    "low": "low for today",
    "wind speed": "wind speed",
    "humidity": "humidity",
    "condition": "conditions"
}
def generate_response(city, state, feature, data):
    # TODO: figure out a better way to phrase the response for "conditions"
    # and also the other responses
    copula = "is" if feature != "condition" else "are"
    return f"The {FULL_NAME[feature]} in {city}, {state} {copula} {data[feature]}"


# This is the function the driver will use to process weather requests.
# It takes in (or will when we're done) the string inputted by the user and returns
# a string for the program to respond with. We might break up the input into multiple
# prompts (what city, what state, etc.) in which case this may change a bit, depending
# on how that works.
def process_request(request):
    parsed = parse_request(request)
    city = parsed["city"]
    state = parsed["state"]

    return generate_response(city, state, parsed["feature"], get_weather(city, state))


# Test
print(process_request(["Portland", "Maine", "condition"]))