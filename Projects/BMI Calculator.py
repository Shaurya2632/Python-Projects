from customtkinter import *

# --- AutoRepeatButton class ---
import threading

class AutoRepeatButton(CTkButton):
    def __init__(self, master, command=None, delay=400, interval=200, **kwargs):
        super().__init__(master, command=self._on_click, **kwargs)
        self._user_command = command
        self._delay = delay / 1000     # Delay in seconds
        self._interval = interval / 10000  # Fixed: Corrected interval divisor
        self._auto_repeat = False
        self._repeat_thread = None

        self.bind("<ButtonPress-1>", self._start_auto_repeat)
        self.bind("<ButtonRelease-1>", self._stop_auto_repeat)
        self.bind("<Leave>", self._stop_auto_repeat)

    def _on_click(self):
        if self._user_command:
            self._user_command()

    def _repeat_func(self):
        threading.Event().wait(self._delay)
        while self._auto_repeat:
            if self._user_command:
                self._user_command()
            threading.Event().wait(self._interval)

    def _start_auto_repeat(self, event):
        self._auto_repeat = True
        self._repeat_thread = threading.Thread(target=self._repeat_func, daemon=True)
        self._repeat_thread.start()

    def _stop_auto_repeat(self, event=None):
        self._auto_repeat = False

# --- BMI Calculator App ---
def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))

def changeWeight(direction):
    w = int(show_weight.get().replace(" Kg", ""))
    if direction == "in":
        w = clamp(w + 1, 25, 200)
    else:
        w = clamp(w - 1, 25, 200)
    show_weight.set(f"{w} Kg")
    calculateBMI()

def changeHeight(direction):
    h = int(show_height.get().replace(" Cm", ""))
    if direction == "in":
        h = clamp(h + 1, 50, 200)
    else:
        h = clamp(h - 1, 50, 200)
    show_height.set(f"{h} Cm")
    calculateBMI()

def calculateBMI(*args):
    try:
        w = int(show_weight.get().replace(" Kg", ""))
        h = int(show_height.get().replace(" Cm", ""))

        bmi = round(w / ((h / 100) ** 2), 1)
        result_label.configure(text=bmi)
        changeColor(bmi)
    except Exception as e:
        result_label.configure(text="")

def changeColor(bmi):
    if bmi < 15:
        col = "dodger blue"
    elif bmi < 25:
        col = "green"
    elif bmi < 30:
        col = "orange"
    else:
        col = "red"
    app.configure(bg_color=col, fg_color=col)

def validate_input(new_val):
    if new_val == "":
        return True
    if new_val.isdigit():
        val = int(new_val)
        return 0 <= val <= 300
    return False

set_appearance_mode("light")

app = CTk()
app.title("BMI Calculator")
app.geometry("300x420")
app.resizable(False, False)
app.configure(bg_color="blue", fg_color="dodger blue")

input_frame = CTkFrame(app, bg_color="white", fg_color="white", width=300, height=220)
input_frame.place(x=0, y=230)

show_weight = StringVar(value="60 Kg")
show_height = StringVar(value="160 Cm")

weight_label = CTkLabel(input_frame, text="Weight ", font=("Calibri", 26, "bold"), text_color="dodger blue")
weight_label.place(x=25, y=30)

weight_value_label = CTkLabel(input_frame, textvariable=show_weight, font=("Calibri", 22), fg_color="white", bg_color="white",
                             width=80, text_color="dodger blue")
weight_value_label.place(x=110, y=33)

AutoRepeatButton(input_frame, text='▲', font=("", 15), width=25, command=lambda: changeWeight("in")).place(x=230, y=18)
AutoRepeatButton(input_frame, text='▼', font=("", 15), width=25, command=lambda: changeWeight("de")).place(x=230, y=55)

height_label = CTkLabel(input_frame, text="Height ", font=("Calibri", 26, "bold"), text_color="dodger blue")
height_label.place(x=25, y=108)

height_value_label = CTkLabel(input_frame, textvariable=show_height, font=("Calibri", 22), fg_color="white", bg_color="white",
                              width=80, text_color="dodger blue")
height_value_label.place(x=110, y=111)

AutoRepeatButton(input_frame, text='▲', font=("", 15), width=25, command=lambda: changeHeight("in")).place(x=230, y=98)
AutoRepeatButton(input_frame, text='▼', font=("", 15), width=25, command=lambda: changeHeight("de")).place(x=230, y=135)

result_label = CTkLabel(app, text="", font=("Calibri", 60, "bold"), text_color="white")
result_label.place(relx=0.5, y=80, anchor="n")

# Update BMI when weight or height changes
show_weight.trace_add("write", calculateBMI)
show_height.trace_add("write", calculateBMI)

calculateBMI()

app.mainloop()
