from concurrent.futures import ThreadPoolExecutor
import time, mouse, keyboard

executor = ThreadPoolExecutor(max_workers=1)

clicking = False
running = True

def clicker():
    while clicking:
        mouse.click()
        time.sleep(0.1)

while running:
    if keyboard.is_pressed("s"):
        if not clicking:
            clicking = True
            executor.submit(clicker)
        else:
            clicking = False
        time.sleep(0.5)

    if keyboard.is_pressed("q"):
        clicking = False
        running = False
        time.sleep(0.5)

    time.sleep(0.01)

executor.shutdown(wait=False)
