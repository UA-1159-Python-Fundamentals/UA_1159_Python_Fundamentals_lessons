import tkinter as tk
from tkinter import font
def get_weather():
    from pyowm import OWM

    API_KEY = 'ef2206ff5da67de63306d0b143e20872'
    # ---------- FREE API KEY examples ---------------------

    _owm = OWM(API_KEY)
    mgr = _owm.weather_manager()

    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place('London,GB')
    w = observation.weather

    label['text'] =f"{w.detailed_status}\n{w.wind()}\n{w.humidity}\n{w.temperature('celsius')}\n{w.rain}\n{w.heat_index}\n{w.clouds}"
    label['font'] = ('Courier', 12)
    label['anchor'] = 'center'

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
                   font=('Courier', 8),
                   command= get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()
