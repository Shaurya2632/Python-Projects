import winreg, pynvml, time, psutil, threading, speedtest, string, cv2
import cpuinfo, platform, mouse, keyboard, math, PyPDF2, re, random, qrcode
from rich.live import Live
from rich.table import Table
from datetime import datetime
from rich import box
from rich.panel import Panel
from fractions import Fraction
from PIL import Image
from rembg import remove
from customtkinter import *
from functools import wraps
from time import perf_counter
from nltk.corpus import words
import subprocess, ctypes, sys, win32com.client

# util

def SystemInfo():

        with Live(refresh_per_second = 1) as live:
            while True:

                table = Table(show_header = False, box = box.MINIMAL, show_lines = True, style = "white")

                table.add_column(width = 15, style = 'blue')
                table.add_column(width = 30, style = "white")

                table.rows.clear()

                cpuInfo = cpuinfo.get_cpu_info()
                table.add_row("Processor ", cpuInfo.get("brand_raw").split("@")[0])
                maxFreq = cpuInfo.get("brand_raw").split("@")[1].replace(" ", "").replace("GHz", " GHz")

                reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
                edition, _ = winreg.QueryValueEx(reg_key, "EditionID")

                table.add_row("OS", f"{platform.system()} {platform.release()} {edition}")

                table.add_row("CPU Usage", f"{psutil.cpu_percent()} %")
                table.add_row("CPU Count", str(psutil.cpu_count()))
                table.add_row("CPU Max Freq", str(maxFreq))
                table.add_row("CPU Freq", str(psutil.cpu_freq().current) + " MHz")

                pynvml.nvmlInit()
                handle = pynvml.nvmlDeviceGetHandleByIndex(0)  # GPU 0

                name = str(pynvml.nvmlDeviceGetName(handle)).replace("b'", "").replace("'", "")
                mem = pynvml.nvmlDeviceGetMemoryInfo(handle)
                used = mem.used // 1024 ** 2
                total = mem.total // 1024 ** 2

                table.add_row("GPU", f"{name}")
                table.add_row("GPU Memory", f"{used} MB / {total} MB")

                memory = psutil.virtual_memory()
                table.add_row("Total Memory", f"{memory.total / (1024 ** 3):.2f} GB")
                table.add_row("Used Memory", f"{memory.used / (1024 ** 3):.2f} GB")
                table.add_row("Memory Usage", f"{memory.percent} %")

                battery = psutil.sensors_battery()
                if battery:
                    table.add_row("Battery", f"{battery.percent} %")
                    table.add_row("Plugged In", str(battery.power_plugged))
                else:
                    table.add_row("Battery", "Not Available")

                    bootTime = psutil.boot_time()

                    currentTime = time.time()

                    upTime = currentTime - bootTime

                    upTime = time.strftime("%H:%M:%S", time.gmtime(upTime))

                    boot = datetime.fromtimestamp(bootTime).strftime('%Y-%m-%d %I:%M:%S %p')
                    table.add_row("Boot Time", boot)

                    table.add_row("Up Time", upTime)

                    SystemInfo = Panel(table, title = "System Info", width = 55, style = "green")

                live.update(SystemInfo)

def AutoClicker(startKey = "s", stopKey = "q", delay = 0.5):

        running = False

        def clicker():
            while running:
                mouse.click()
                time.sleep(delay)

        while True:

            if keyboard.is_pressed(startKey):
                running = not running
                if running: threading.Thread(target = clicker).start()
                time.sleep(0.3)

            elif keyboard.is_pressed(stopKey):
                running = False
                break

def MousePos(minimize = 1, bigsize = 1, loop = True, split = ", "):

        try:

            if loop:

                while True:
                    x = int((mouse.get_position()[0] / minimize) * bigsize)
                    y = int((mouse.get_position()[1] / minimize) * bigsize)

                    os.system("cls")
                    print(f"Mouse position: ({x}{split}{y})")
                    time.sleep(0.050)

            else:
                x = int((mouse.get_position()[0] / minimize) * bigsize)
                y = int((mouse.get_position()[1] / minimize) * bigsize)

                print(f"Mouse position: ({x}{split}{y})")

        except Exception as e:
            print(e)

def InternetSpeed():

        speed = speedtest.Speedtest()
        speed.get_servers()

        download = round(speed.download() / 10 ** 6, 2)
        upload = round(speed.upload() / 10 ** 6, 2)

        return upload, download, "Mbps"

def LiveTime():

        while True:
            os.system('cls')
            print(datetime.now().strftime("%I:%M:%S %p"))
            time.sleep(1)

def bgRemover(path):

        name = (path.split("\\")[-1]).split(".")[0]
        type = (path.split("\\")[-1]).split(".")[1]

        remove(Image.open(path)).save(path.replace(name, f"{name}_bgRemove").replace(type, "png"))

def imageResizer(image_path, width, height):

    name = (image_path.split("\\")[-1]).split(".")[0]
    final_path = image_path.replace(name, f"{name}_Resized")

    image = cv2.imread(image_path)
    image = cv2.resize(image, (width, height))
    cv2.imwrite(final_path, image)

def matrixPos(index, col):

        return [index // col, index % col]

def sec2Format(seconds):

        hour = int(seconds // 3600)
        min = int((seconds % 3600) // 60)
        sec = seconds % 60

        return f"{hour:02} : {min:02} : {sec:06.3f}"

def sec2MilliFormat(seconds):

        min = int((seconds % 3600) // 60)
        sec = int(seconds % 60)
        milli = round((seconds - int(seconds)) * 1000)

        return f"{min:02} : {sec:02} : {milli:03}"

def sizeOf(obg, Unit="MB", DecPlace = 4):

        size = sys.getsizeof(obg)

        return {
            "B": size,
            "KB": round(size / 1024, 4),
            "MB": round(size / (1024 ** 2), DecPlace),
            "GB": round(size / (1024 ** 3), DecPlace),
            "TB": round(size / (1024 ** 4), DecPlace)
        }[Unit.upper()]

def qrCodeGenerator(file_path, url):

    qr = qrcode.QRCode(box_size = 10, border = 1)
    qr.add_data(url)

    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save(file_path)

def batchRunner(*files):

    for file in files:

        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()

        except:
            is_admin = False

        if not is_admin:

            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{__file__}" "{file}"', None, 1)
            sys.exit()

        else:
            subprocess.run(f'"{file}"', shell = True)

def speak(message = ""):

    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    voices = speaker.GetVoices()

    speaker.Voice = voices.Item(0)
    speaker.Speak(message)

# advMath

def isArmstrong(num):

        validator = 0
        l = len(str(num))
        Original_num = num

        while num > 0:
            validator += pow(num % 10, l)
            num //= 10

        return validator == Original_num

def Fibonacci_Series(n):

        Fib = [0, 1]

        while (next_Fib := Fib[- 1] + Fib[- 2]) <= n:
            Fib.append(next_Fib)

        return Fib

def Root(num, n):

        return pow(num, 1 / n)

def Exponent(num, base = 2, format = True):

        symbols = ['¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']

        n = round(math.log(num, base))

        if base ** n == num:
            if format:
                return f"{base}{symbols[n - 1]}"
            else:
                return f"{base} ^ {n}"

        if format:
            return f"{base}{symbols[n - 1]}"
        else:
            return f"{base} ^ {n}"

def Divisor(n):

        return [i for i in range(1, n + 1) if n % i == 0]

def Probability(Favorable_outcomes, Total_outcomes):

        return Fraction(Favorable_outcomes / Total_outcomes).limit_denominator()

def BMICalculator(weight, height):

    return weight / height ** 2

# string

def caseChange(string, case = "", upperLimit = 0, lowerLimit = 0):

          def Case2Snake(string):

              return string.replace(" ", "_")

          def Case2Camel(string):

              string = string.title()
              listOfChar = [char for i, char in enumerate(string) if string[i] != " "]
              listOfChar[0] = listOfChar[0].lower()

              return "".join(listOfChar)

          def Case2Kabab(string):

              return string.replace(" ", "-")

          def Case2UpperUntil(string, limit):

              listChr = list(string)

              for i in range(min(len(string), limit)):
                  listChr[i] = string[i].upper()

              return "".join(listChr)

          def Case2LowerUntil(string, limit):

              listChr = list(string)

              for i in range(min(len(string), limit)):
                  listChr[i] = string[i].lower()

              return "".join(listChr)

          case = case.lower()

          converter = {
              'snake': lambda string: Case2Snake(string),
              'camel': lambda string: Case2Camel(string),
              'kabab': lambda string: Case2Kabab(string)
          }

          if upperLimit:
              return Case2UpperUntil(string, upperLimit)

          elif lowerLimit:
              return Case2LowerUntil(string, lowerLimit)

          else:
              return converter[case](string)

def reverseWords(sentence):

    listOfWords = sentence.split()
    return " ".join((listOfWords[::-1]))

def UPPER(string, ind = None, slice_ = None):

          li = list(string)

          if ind:
              li[ind] = li[ind].upper()
          elif slice_ and isinstance(slice_, slice):
              li[slice_] = list(string[slice_].upper())

          return "".join(li)

def LOWER(string, ind = None, slice_ = None):

          li = list(string)

          if ind:
              li[ind] = li[ind].lower()

          elif slice_ and isinstance(slice_, slice):
              li[slice_] = list(string[slice_].lower())

          return "".join(li)

# file

def createFile(loc):

           f = os.open(loc, os.O_CREAT)
           os.close(f)

def deleteFile(loc):

           os.remove(loc)

def renameFile(old, new):

           os.rename(old, new)

def writeData(loc, toWrite):

           with open(loc, "w") as f:
               f.write(toWrite)

def readData(loc):

           with open(loc, "r") as f:
               return f.read()

def appendData(loc, toAppend):

           with open(loc, "a") as f:
               f.write(toAppend)

def pdfMerger(pdfs, dst):

    with PyPDF2.PdfMerger() as merger:

        for pdf in pdfs:

            merger.append(pdf)

        merger.write(dst)

# decorator

def funcTime(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            start: float = perf_counter()
            func(*args, **kwargs)
            end: float = perf_counter()

            print(f"{func.__name__}() took {(end - start):.3f} S")

        return wrapper

class Calculator(CTk):

    def __init__(self):

        super().__init__()
        self.title("Calculator")
        self.geometry("270x360")
        self.resizable(False, False)

        color = "grey14"

        self.display = CTkEntry(self, width = 250, height = 50, font = ("Arial", 24), justify = "right",
                           border_color = color, fg_color = color)

        self.display.insert(END, "0")
        self.display.configure(state = "disabled")
        self.display.place(x = 10, y = 10)

        self.expression = ""



        buttons = [
                   ('C', 10, 70), ('=', 60, 70), ('⌫', 160, 70),                     ('÷', 220, 120),
                   ('6', 10, 120), ('7', 60, 120), ('8', 110, 120), ('9', 160, 120), ('-', 220, 170),
                   ('2', 10, 170), ('3', 60, 170), ('4', 110, 170), ('5', 160, 170), ('x', 220, 220),
                   ('1', 10, 220), ('0', 60, 220), ('.', 110, 220),                  ('+', 220, 270),

                   ('π', 10, 310), ('e', 60, 310), ('Φ', 110, 310), ('γ', 160, 310),
                  ]

        self.create_Buttons(buttons)

    def create_Buttons(self, buttons):

        for (text, x, y) in buttons:

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
                self,
                text = text,
                width = width,
                fg_color = fg_color,
                height = 40,
                font = ("Arial", 20),
                hover_color = hov_color,
                command = lambda val = text: self.calc(val)
            ).place(x = x, y = y)

    def calc(self, val):

            valueToReplace = {
                'x': "*",
                '÷': "/",
                'π': f"{round(math.pi, 2)}",
                'e': f"{round(math.e, 2)}",
                'Φ': '1.61803',
                'γ': '0.57721'

            }

            if val in valueToReplace: val = valueToReplace[val]

            if val == "C":
                val = ""
                self.expression = ""

            if val == '⌫':
                val = ""
                self.expression = self.expression[:-1]

            if val == "=":

                try:
                    self.expression = eval(self.expression)

                    if ".0" in str(self.expression):
                        self.expression = int(self.expression)

                    else:
                        self.expression = round(self.expression, 2)

                    self.expression = str(self.expression)

                    self.display.configure(state = "normal")
                    self.display.delete(0, END)
                    self.display.configure(state = "disabled")
                except:
                    self.display.configure(state = "normal")
                    self.display.delete(0, END)
                    self.display.insert(0, "Error")
                    self.display.configure(state = "disabled")

            else:
                self.expression = self.expression + val

            self.display.configure(state = 'normal')
            self.display.delete(0, END)
            self.display.insert(END, self.expression)
            self.display.configure(state = "disabled")

    def start(self):
        self.mainloop()

    def stop(self):
        self.quit()

# passwords

class Password:

    def __init__(self, pwd = "", text = ""):

        self.__weak_passwords = [
        "123456",
        "password",
        "123456789",
        "qwerty",
        "12345678",
        "111111",
        "123123",
        "abc123",
        "password1",
        "1234",
        "qwerty123",
        "admin",
        "letmein",
        "iloveyou",
        "000000"
    ]

        self.__strength = "None"

        self.__pwd = pwd

        self.__text = text

        self.VERY_WEAK = "Very Weak"
        self.WEAK = "Weak"
        self.MODERATE = "Moderate"
        self.STRONG = "Strong"
        self.VERY_STRONG = "Very Strong"
        self.INVALID = "Invalid"

        self.ALL = [self.VERY_WEAK, self.WEAK, self.MODERATE, self.STRONG, self.VERY_STRONG]

    def Strength(self, pwd = ""):

        if pwd:
            self.__pwd = pwd

            # 1. Only spaces or has spaces
        if re.search(r"\s", self.__pwd) or len(self.__pwd) == 0:
            self.__strength = self.INVALID

            # 2. Very strong: upper, lower, digit, special
        elif re.search(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W)", self.__pwd):
            self.__strength = self.VERY_STRONG

            # 3. Strong: either uppercase + something OR long enough
        elif re.search(r"[A-Z]", self.__pwd) and len(self.__pwd) >= 8:
            self.__strength = self.STRONG

            # 4. Moderate: has digit or special
        elif re.search(r"\d", self.__pwd) or re.search(r"\W", self.__pwd):
            self.__strength = self.MODERATE

            # 5. Weak: all lowercase
        elif self.__pwd.islower():
            self.__strength = self.WEAK

            # 6. Very weak: same char repeated or common weak passwords
        elif self.__pwd.count(self.__pwd[0]) == len(self.__pwd) or self.__pwd in self.__weak_passwords:
            self.__strength = self.VERY_WEAK

        elif self.__pwd.count(self.__pwd[0]) == len(self.__pwd):
            self.__strength = self.VERY_WEAK

        else:
            self.__strength = self.VERY_WEAK

        return self.__strength

    def identifier(self, text = "", reqStrength = None):

        if text:
            self.__text = text

        wordList = self.__text.split()

        normal_words = set(words.words())

        passwords = []

        if not reqStrength:
            reqStrength = [self.STRONG, self.VERY_STRONG]

        pwdStrength = list(map(self.Strength, wordList))

        for word, strength in zip(wordList, pwdStrength):

            if strength in reqStrength and word.lower() not in normal_words:
                passwords.append(word)

        return passwords

class Secure:

    def __init__(self, password):

        self.__PlaneText = ""
        self.__EncryptedText = ""

        self.__defaultPassword = 1290

        if int(password) != self.__defaultPassword:
            raise ValueError("Please enter a valid password")

        self.Unicode =  list(string.punctuation + string.digits)

    def Encrypter(self, plane_text=''):

        self.__PlaneText = plane_text
        self.__EncryptedText = reverseWords(self.__PlaneText)

        listOfChr = list(self.__EncryptedText)
        listOfUnicode = []
        encryptedList = []

        for _ in range(0, len(listOfChr)):
            listOfUnicode.append(self.Unicode[random.randint(0, len(self.Unicode)-1)])

        for i in range(len(listOfChr)):
            encryptedList.append(listOfChr[i])
            encryptedList.append(listOfUnicode[i])

        self.__EncryptedText = "".join(encryptedList)

        encryptedList = self.__EncryptedText.split()

        for i, word in enumerate(self.__EncryptedText.split()):
            encryptedList[i] = word[::-1]

        self.__EncryptedText = " ".join(encryptedList)

        return self.__EncryptedText

    def Decrypter(self, encrypted_text=''):

       self.__EncryptedText = encrypted_text
       self.__PlaneText = reverseWords(encrypted_text[::-1])

       for word in self.__PlaneText:

           if word in self.Unicode:
               self.__PlaneText = self.__PlaneText.replace(word, "")

       self.__PlaneText = reverseWords(self.__PlaneText)

       return self.__PlaneText

    @property
    def password(self):

        return self.__defaultPassword

    @password.setter
    def password(self, new_pwd):

        self.__defaultPassword = new_pwd
