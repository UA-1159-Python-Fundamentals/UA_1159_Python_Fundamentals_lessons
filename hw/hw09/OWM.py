from pyowm import OWM

# weather_details = [1,2,3,4,5,6,7]

def get_weather():

    API_KEY = 'ef2206ff5da67de63306d0b143e20872'
    # ---------- FREE API KEY examples ---------------------

    owm = OWM(API_KEY)
    mgr = owm.weather_manager()


    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place('London,GB')
    w = observation.weather
    
    # global weather_details

    weather_details = [
        f"Detailed status: {w.detailed_status}",
        f"Wind: {w.wind()}",
        f"Humidity: {w.humidity}",
        f"Temperature: {w.temperature('celsius')}",
        f"Rain: {w.rain}",
        f"Heat index: {w.heat_index}",
        f"Clouds: {w.clouds}"]
    
    return weather_details
    # print(weather_details)

# get_weather()

# __ALL__ = ['get_weather', 'weather_details']
__ALL__ = ['get_weather']



