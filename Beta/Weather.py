import requests
from rich.console import Console
import customtkinter as _

Api_Key = "ea1b7e8a9ab18916c241eba16c9ba876"

loc = "Visnagar"

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={loc}&units=imperial&APPID={Api_Key}")

rprint = lambda x: Console().print(x)

temp = weather_data.json()['main']["temp"]

rprint(f"{temp} °F")

