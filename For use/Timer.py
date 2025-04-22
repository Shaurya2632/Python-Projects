import winsound, os, time, re, pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 300)

def TextToSpeech(text, hour, min, sec):
    engine.say(text.replace(f"0{hour}", f"{hour}")
                   .replace(f"0{min}", f"{min}")
                   .replace(f"0{sec}", f"{sec}")), engine.runAndWait()

def Timer(format):

    numbers = re.findall(r"\d+", format)
    
    while len(numbers) < 3:
            numbers.insert(0, "0")

    hour, min, sec = map(int, (num.zfill(2) for num in numbers))
    
    if hour > 23 : hour = 24
    if min > 59: min = 59
    if sec > 59: sec = 59
    
    while True:
        os.system("cls")
        if hour == min == sec == 0: break

        print(f"{hour:02} : {min:02} : {sec:02}")

        time.sleep(1)
        sec -= 1
        
        if sec == -1:
            min -= 1
            sec = 59
            
        if min == -1:
            hour -= 1
            min = 59

    print("\rTimer Ended")
    
    play = winsound
    delay = time
    
    for i in range(5):
        play.Beep(800, 200)
        delay.sleep(0.000001)
        play.Beep(800, 200)
        delay.sleep(1.8)
        

def NotDisplayTimer(format):

    numbers = re.findall(r"\d+", format)

    while len(numbers) < 3:
        numbers.insert(0, "0")

    hour, min, sec = map(int, (num.zfill(2) for num in numbers))

    if hour > 23: hour = 24
    if min > 59: min = 59
    if sec > 59: sec = 59

    while True:

        if hour == min == sec == 0: break

        time.sleep(1)
        sec -= 1

        if sec == -1:
            min -= 1
            sec = 59

        if min == -1:
            hour -= 1
            min = 59

    play = winsound
    delay = time

    for _ in range(5):
          play.Beep(800, 200)
          delay.sleep(0.000001)
          play.Beep(800, 200)
          delay.sleep(1.8)

print(Timer("40"))