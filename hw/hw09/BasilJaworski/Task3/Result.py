import tkinter as tk
from pyowm import OWM
from tkinter import CENTER, LEFT, font


def get_wether():
  global label
  
  try:
    wether_city = entry_field.get()
    wether_text = ""

    observation = mgr.weather_at_place(wether_city)
    w = observation.weather
  
    wether_text += "CLOUDS --> "
    wether_text += str(w.detailed_status) + "\n"
    wether_text += "WIND: --> "
    wether_text += str(w.wind()) + "\n"
    wether_text += "HUMIDITY: --> "
    wether_text += str(w.humidity) + "\n"
    wether_text += "t°: --> "
    wether_text += str(w.temperature('celsius')) + "\n"
    wether_text += "RAIN: --> "
    wether_text += str(w.rain) + "\n"
    wether_text += "HEAT_INDEX: --> "
    wether_text += str(w.heat_index) + "\n"
    wether_text += "CLOUDS: --> "
    wether_text += str(w.clouds) + "\n"
  except:
    wether_text = "Error the city not found!"
    
  label.config(text=wether_text)


API_KEY = 'ef2206ff5da67de63306d0b143e20872'

owm = OWM(API_KEY)
mgr = owm.weather_manager()


HEIGHT = 350
WIDTH = 450


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier',  8),
                   command=get_wether)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 8), anchor="nw", justify=LEFT,)
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()