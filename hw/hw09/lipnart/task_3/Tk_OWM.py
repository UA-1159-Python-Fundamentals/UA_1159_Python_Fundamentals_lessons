import tkinter as tk
from tkinter import font
import OWM

HEIGHT = 350
WIDTH = 450


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


def get_weather(city):
    l = OWM.get_response(city)
    label["text"] = (
        f"\t Status: {l[0]}\n \
        Speed: {l[1]['speed']} m/s\n \
        Deg: {l[1]['deg']}\n \
        Gust: {l[1]['gust']}\n \
        Humidity: {l[2]}%\n \
        Temperature: {l[3]['temp']}°C\n \
        Rain: {l[4]}\n \
        Heat_index: {l[5]}\n \
        Clouds: {l[6]}%"
    )


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry_field = tk.Entry(frame, font=("Courier", 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(
    frame,
    text="Get Weather",
    bg="gray",
    fg="black",
    font=("Courier", 8),
    command=lambda: get_weather(entry_field.get()),
)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg="gold", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(
    lower_frame, font=("Courier", 14), text="", justify="left", compound="left"
)
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()
