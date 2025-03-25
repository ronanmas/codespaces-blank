from bs4 import BeautifulSoup as soup
import requests

def getcoords(city, state):

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

    coords = {"lat":lat, "long":long}
    return coords



def condition_simple(city,state,type,class_):
    url = f'https://www.wunderground.com/weather/us/{state}/{city.lower()}'
    req = requests.get(url)
    web_page = req.content
    web = soup(web_page,'html.parser')
    name_box = web.find(type, class_)
    name = name_box.text.split() 
    dict = {"high": name}
    return dict

def info(condition, city, state):
    if condition == "coordinates":
        condition = getcoords(city,state,)
    elif condition == "time":
        condition = condition_simple(city,state,'p','timestamp')
    elif condition == "high":
        condition = condition_simple(city,state,'span','hi')
    elif condition == "low":
        condition = condition_simple(city,state,'span','lo')
    elif condition == "temperature":
        next
        # condition = condition_simple('portland','me','span','test-true wu-unit wu-unit-temperature is-degree-visible ng-star-inserted')
    elif condition == "feels like":
        condition = condition_simple(city,state,'span','temp')
    elif condition == "condition":
        condition = condition_simple(city,state,'div','condition-icon small-6 medium-12 columns')
    elif condition == "humidity":
        condition = condition_simple(city,state,'span','test-false wu-unit wu-unit-humidity ng-star-inserted')
    elif condition == "gusts":
        condition = condition_simple(city,state,'span','test-false wu-unit wu-unit-speed ng-star-inserted')
    elif condition == "wind speed":
        condition = condition_simple(city,state,'header','wind-speed')
    return condition


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


coords = info("coordinates", 'portland', 'me')
print(coords)

time = info('time', 'portland', 'me')
print(time)


high = info('high', 'portland', 'me')
print(high)

low = info('low', 'portland', 'me')
print(low)

temp = info('temperature', 'portland', 'me')
print(temp)

condition = info('condition', 'portland', 'me')
print(condition)

feels_like = info('feels like', 'portland', 'me')
print(feels_like)

humidity = info('humidity', 'portland', 'me')
print(humidity)

gusts = info('gusts', 'portland', 'me')
print(gusts)

wind_speed = info('wind speed', 'portland', 'me')
print(wind_speed)












# coords = getcoords('portland', 'me')
# time = condition_simple('portland','me','p','timestamp', time)
# high = condition_simple('portland','me','span','hi', high)
# low = condition_simple('portland','me','span','lo', low)
# temp = condition_simple('portland','me','span','test-true wu-unit wu-unit-temperature is-degree-visible ng-star-inserted', temp)
# feels_like = condition_simple('portland','me','span','temp', feels_like)
# condition = condition_simple('portland','me','div','condition-icon small-6 medium-12 columns', condition)
# humidity = condition_simple('portland','me','span','test-false wu-unit wu-unit-humidity ng-star-inserted', humidity)
# gusts = condition_simple('portland','me','span','test-false wu-unit wu-unit-speed ng-star-inserted', gusts)
# wind_speed = condition_simple('portland','me','header','wind-speed', wind_speed)

# print(coords)
# print(time[1:8]) 
# print(high)
# print(low)
# # print(temp) 
# print(feels_like)
# print(condition)
# print(humidity[0])
# print(wind_speed)
# print(gusts[0])


# def condition_multi(url,type, class_,name):
#     req = requests.get(url)
#     web_page = req.content
#     web = soup(web_page,'html.parser')
#     name = web.find_all(type, class_)
#     return name

# temp = condition_multi('https://www.wunderground.com/weather/us/me/portland','span','test-true wu-unit wu-unit-temperature is-degree-visible ng-star-inserted', temp)
# print(temp[8])









# Next Funciton
# for a certain place in ("","") order, return the desired outputs:
        # get_current_wx(portland, me) -> {'time': ' 8:46 AM EDT on May 3, 2021', 
        # 'hi': '55°', 
        # 'lo': '44°', 
        # 'temp': '52', 
        # 'feels': '52°', 
        # 'condition': 'Mostly Cloudy', 
        # 'humidity': '52', 
        # 'wind_dir': 'NE', 
        # 'wind_spd': '8', 
        # 'gusts': '12 mph'}



