import sys, os, pyautogui, time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Utility import MousePos

def even(n):
    was_odd = n % 2 == 1
    return n + 1 if was_odd else n

minimize = 1
bigsize = .1

screen_width, screen_height = pyautogui.size() 
scaled_width = even(int((screen_width / minimize) * bigsize))
scaled_height = even(int((screen_height / minimize) * bigsize))

print(f"resolution: {scaled_width} x {scaled_height}")

while True:

    os.system("cls")
    print(f"Scaled Screen Resolution: {scaled_width} x {scaled_height}")
    MousePos(minimize, bigsize, False, " | ")
    time.sleep(0.050)