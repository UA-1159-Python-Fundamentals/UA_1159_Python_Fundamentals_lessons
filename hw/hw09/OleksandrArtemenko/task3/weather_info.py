import tkinter as tk
from tkinter import font
from pyowm.commons.exceptions import NotFoundError
import OWM


def get_weather_info():
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
                       command=lambda: update_label())

    button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

    lower_frame = tk.Frame(root, bg='gold', bd=10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

    label = tk.Label(lower_frame, font=('Courier', 8))
    label.place(relx=0, rely=0, relwidth=1, relheight=1)

    def update_label():
        try:
            w = OWM.get_weather(entry_field.get())
            weather_info = {
                "location": entry_field.get(),
                "general": w.detailed_status,
                "wind": w.wind(),
                "humidity": w.humidity,
                "temperature": w.temperature('celsius'),
                "rain": w.rain if w.rain else "no rain",
                "heat": w.heat_index if w.heat_index is not None else "no heat",
                "cloud level": w.clouds
            }
        except NotFoundError:
            weather_info = f"There is no such location '{entry_field.get()}' and the weather cannot be shown"

        label.config(text=str(weather_info).replace(",", "\n").replace("{", "")
                     .replace("}", ""), wraplength=300, justify="left")
        label.pack()

    root.mainloop()


if __name__ == "__main__":
    get_weather_info()
