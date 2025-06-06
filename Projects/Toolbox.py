
from customtkinter import *
import hashlib, pyperclip, qrcode # type: ignore

from Utility.math import *
import math

set_appearance_mode("Dark")
set_default_color_theme("blue")

expression = ""

def calc(val):

    valueToReplace = {
        'x': "*",
        '÷': "/",
        'π': f"{math.pi}",
        'e': f"{math.e}",
        'Φ': '1.61803',
        'γ': '0.57721'

    }

    global expression

    if val in valueToReplace: val = valueToReplace[val]

    if val == "C":
        val = ""
        expression = ""

    if val == '⌫':
        val = ""
        expression = expression[:-1]

    if val == "=":

        try:
            expression = eval(expression)

            if ".0" in str(expression):
                expression = int(expression)

            else:
                expression = round(expression * 100) / 100

            expression = str(expression)

            display.configure(state = "normal")
            display.delete(0, END)
            display.configure(state = "disabled")
        except:
            display.configure(state = "normal")
            display.delete(0, END)
            display.insert(0, "Error")
            display.configure(state = "disabled")

    else:
        expression = expression + val

    display.configure(state = 'normal')
    display.delete(0, END)
    display.insert(END, expression)
    display.configure(state = "disabled")

def advCalc():
    try:
        a = float(eval(num1_entry.get()))
        b = float(eval(num2_entry.get()))
        opr = option.get()

        if "E^" not in opr: opr = opr.replace("^", "**")

        notToCalc = ['√', 'E^']

        AdvCalculation = {
            '√': lambda n, p: Root(n, p),
            'E^': lambda n, b: Exponent(n ,b , format = False)
        }

        exp = f"{a} {opr} {b}"

        if opr not in notToCalc: result = eval(exp)

        else: result = AdvCalculation[opr](a, b)

        calc_result.configure(state = "normal")
        calc_result.delete(0, END)
        calc_result.insert(0, str(result))
        calc_result.configure(state = "disabled")
    except:
        calc_result.configure(state = "normal")
        calc_result.delete(0, END)
        calc_result.insert(0, "Error")
        calc_result.configure(state = "disabled")

def generate_hash():

    pwd = pwdEntry.get()
    algo = algos.get()

    hashed = ""

    try:
        output.configure(state = "normal")
        if pwd != "": hashed = hash_funcs[algo](pwd)
        output.delete("0.0", "end")
        output.insert("0.0", hashed)
        output.configure(state = "disabled")
    except Exception as e:
        output.configure(state = "normal")
        output.delete("0.0", "end")
        output.insert("0.0", f"Error: {e}")
        output.configure(state = "disabled")

def copy_hash():
    pyperclip.copy(output.get("0.0", "end").strip())

def clear_hash():

    pwdEntry.delete(0, END)
    output.configure(state = "normal")
    output.delete("0.0", END)
    output.configure(state = "disabled")

def generate_QRcode():
    qr = qrcode.QRCode(box_size = 10, border = 1)
    qr.add_data(url.get())
    img = qr.make_image(fill_color = "black", back_color = "white").convert("RGB")

    qrcode_ = CTkImage(light_image = img, dark_image = img, size = (150, 150))

    qrcode_display = CTkLabel(qrcodeGenerator, image = qrcode_, font = ("Console", 20), text = "")

    qrcode_display.configure(image = qrcode_)
    qrcode_display.place(x = 105, y = 160)

app = CTk()
app.title("ToolBox")
app.geometry("1070x380")
app.resizable(False, False)

# === Left: Calculator Frame ===
Calc = CTkFrame(app, width=270, height=360, corner_radius=10)
Calc.place(x=10, y=10)

display = CTkEntry(Calc, width=250, height=50, font=("Arial", 24), justify= "right", border_color = "grey17", fg_color = "grey17")
display.insert(END, "0")
display.configure(state = "disabled")
display.place(x=10, y=10)

calc_buttons = [
    ('C', 10, 70), ('=', 60, 70), ('⌫', 160, 70),                     ('÷', 220, 120),
    ('6', 10, 120), ('7', 60, 120), ('8', 110, 120), ('9', 160, 120), ('-', 220, 170),
    ('2', 10, 170), ('3', 60, 170), ('4', 110, 170), ('5', 160, 170), ('x', 220, 220),
    ('1', 10, 220), ('0', 60, 220), ('.', 110, 220),                  ('+', 220, 270),

    ('π', 10, 310), ('e', 60, 310), ('Φ', 110, 310), ('γ', 160, 310),
]

for (text, x, y) in calc_buttons:

    fg_color = "grey22"
    width = 40
    hov_color = "grey15"

    if text == "C":
        fg_color = 'red'
        hov_color = "dark red"

    if text == "=":
        fg_color = "lime green"
        hov_color = 'dark green'
        width = 90

    if text == '⌫':
        fg_color = "dodger blue"
        hov_color = "blue"
        width = 100

    if text in "+-x÷":
        fg_color = "grey30"
        hov_color = "grey20"

    CTkButton(
        Calc,
        text=text,
        width=width,
        fg_color = fg_color,
        height=40,
        font = ("Arial", 20),
        hover_color = hov_color,
        command=lambda val=text:calc(val)
    ).place(x=x, y=y)

# === Right: Function Calculator Frame ===
AdvCalc = CTkFrame(app, width=400, height=140, corner_radius=10)
AdvCalc.place(x=290, y=10)

CTkLabel(AdvCalc, text= "Number 1").place(x=10, y=10)
num1_entry = CTkEntry(AdvCalc, width=140)
num1_entry.place(x=80, y=10)

CTkLabel(AdvCalc, text= "Number 2").place(x=10, y=50)
num2_entry = CTkEntry(AdvCalc, width=140)
num2_entry.place(x=80, y=50)

func = ['+', '-', '*', '/', '^', 'E^', '√']

option = CTkOptionMenu(AdvCalc, width=100, values=func)
option.place(x=230, y=10)
option.set("Function")

ans = CTkLabel(AdvCalc, text = "Answer", font = ("Arial", 15)).place(x = 10, y = 90)

calc_result = CTkEntry(AdvCalc, width=260, state = "disabled")
calc_result.place(x=80, y=90)

calcBT = CTkButton(AdvCalc, text= "=", width=100, command=advCalc, font = ("Arial", 12), fg_color = 'green3',
                   hover_color = "green2", text_color = "white")
calcBT.place(x=230,y=50)

# === Bottom: Password Hasher Frame ===

hashConvertor = CTkFrame(app, width=400, height=210, corner_radius=10)
hashConvertor.place(x=290, y=160)

hash_funcs = {
    "MD5":         lambda p: hashlib.md5(p.encode()).hexdigest(),
    "SHA1":        lambda p: hashlib.sha1(p.encode()).hexdigest(),
    "SHA224":      lambda p: hashlib.sha224(p.encode()).hexdigest(),
    "SHA256":      lambda p: hashlib.sha256(p.encode()).hexdigest(),
    "SHA384":      lambda p: hashlib.sha384(p.encode()).hexdigest(),
    "SHA512":      lambda p: hashlib.sha512(p.encode()).hexdigest(),
    "SHA3_224":    lambda p: hashlib.sha3_224(p.encode()).hexdigest(),
    "SHA3_256":    lambda p: hashlib.sha3_256(p.encode()).hexdigest(),
    "SHA3_384":    lambda p: hashlib.sha3_384(p.encode()).hexdigest(),
    "SHA3_512":    lambda p: hashlib.sha3_512(p.encode()).hexdigest(),
    "SHAKE_128":   lambda p: hashlib.shake_128(p.encode()).hexdigest(64),
    "SHAKE_256":   lambda p: hashlib.shake_256(p.encode()).hexdigest(64),
    "BLAKE2S":     lambda p: hashlib.blake2s(p.encode()).hexdigest(),
    "BLAKE2B":     lambda p: hashlib.blake2b(p.encode()).hexdigest(),
    "RIPEMD160":   lambda p: hashlib.new("ripemd160", p.encode()).hexdigest(),
    "WHIRLPOOL":   lambda p: hashlib.new("whirlpool", p.encode()).hexdigest(),
    "SM3":         lambda p: hashlib.new("sm3", p.encode()).hexdigest(),
    "MD4":         lambda p: hashlib.new("md4", p.encode()).hexdigest(),
    "TIGER":       lambda p: hashlib.new("tiger", p.encode()).hexdigest(),
    "GOST":        lambda p: hashlib.new("gost", p.encode()).hexdigest(),
    "STREEBOG256": lambda p: hashlib.new("streebog256", p.encode()).hexdigest(),
    "STREEBOG512": lambda p: hashlib.new("streebog512", p.encode()).hexdigest(),
    "HAVAL128_3":  lambda p: hashlib.new("haval128_3", p.encode()).hexdigest(),
    "HAVAL160_4":  lambda p: hashlib.new("haval160_4", p.encode()).hexdigest(),
    "HAVAL192_5":  lambda p: hashlib.new("haval192_5", p.encode()).hexdigest(),
}

CTkLabel(hashConvertor, text= "Password Hasher", font=("Arial", 16)).place(x=10, y=10)

pwdEntry = CTkEntry(hashConvertor, placeholder_text= "Enter Password", width=220)
pwdEntry.place(x=10, y=50)

algos = CTkOptionMenu(hashConvertor, width=150, values=list(hash_funcs.keys()))
algos.place(x=240, y=50)

output = CTkTextbox(hashConvertor, width=290, height=110, state = "disabled")
output.place(x=100, y=90)

CTkButton(hashConvertor, text= "Generate", command=generate_hash, width=70).place(x=10, y=90)
CTkButton(hashConvertor, text= "Copy", command=copy_hash, width=70).place(x=10, y=130)
CTkButton(hashConvertor, text= "Clear", command=clear_hash, width=70).place(x=10, y=170)

# === Right: Qrcode Generator Frame ===

qrcodeGenerator = CTkFrame(app, width = 360, height = 360)
qrcodeGenerator.place(x = 700, y = 10)

CTkLabel(qrcodeGenerator, text = "Qrcode Generator", font = ("Arial", 20)).place(x = 105, y = 20)

url = CTkEntry(qrcodeGenerator, placeholder_text = "Enter URL", text_color = "white", width = 250)
url.place(x = 10, y = 80)

generate = CTkButton(qrcodeGenerator, text = "Generate", font = ("Console", 16), width = len("Generate"), command = generate_QRcode)
generate.place(x = 270, y = 80)

app.mainloop()