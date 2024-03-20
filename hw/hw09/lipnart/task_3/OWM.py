from pyowm import OWM

def get_response(city):
    API_KEY = 'ef2206ff5da67de63306d0b143e20872'
    # ---------- FREE API KEY examples ---------------------

    owm = OWM(API_KEY)
    mgr = owm.weather_manager()


    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place(str(city))
    w = observation.weather

    return w.detailed_status, w.wind(), w.humidity, w.temperature('celsius'), w.rain, w.heat_index, w.clouds

# print(get_response("Kyiv"))




