import os, subprocess
from Timer import NotDisplayTimer
from tkinter import *

def Break():

   Apps = [
    "chrome.exe",
    "vlc.exe",
    "python.exe",
    "notepad++.exe",
    "toolbox.exe",
    "fdm.exe",
    "git.exe",
    "flow.exe",
    "glaryutilities.exe",
    "aimp.exe",
    "everything.exe",
    "memreduct.exe",
    "partitionwizard.exe",
    "winrar.exe",
    "WiseProgramUninstaller.exe",
    "vmware.exe",
    "fontviewer.exe",
    "leetcode.exe",
    "intellij64.exe",
    "code.exe",
    "webstorm64.exe",
    "brave.exe",
    "firefox.exe",
    "teams.exe",
    "onenote.exe",
    "powershell.exe",
    "cmd.exe",
    "obs64.exe",
    "audacity.exe",
    "taskmgr.exe",
    "discord.exe",
    "steam.exe",
    "notion.exe",
    "anki.exe",
    "postman.exe",
    "gparted.exe",
    "chatgpt.exe",
    "sublime_text.exe",
    "devcpp.exe",
    "rider64.exe",
    "androidstudio64.exe",
    "unityhub.exe",
    "unrealengine.exe",
    "cmake-gui.exe",
    "geany.exe",
    "xampp-control.exe",
    "winscp.exe",
    "putty.exe",
    "taskcoach.exe",
    "trello.exe",
    "7zFM.exe",
    "calibre.exe",
    "krita.exe",
    "gimp.exe",
    "inkscape.exe",
    "blender.exe",
    "cpu-z.exe",
    "hwmonitor.exe",
    "sharex.exe",
    "screenpresso.exe",
    "rescuetime.exe",
    "f.lux.exe",
    "teamviewer.exe",
    "anydesk.exe",
    "rufus.exe",
    "ventoy.exe",
    "procexp.exe",
    "autoruns.exe",
    "tcpview.exe",
    "glasswire.exe",
    "wireshark.exe",
    "sandboxie.exe",
    "launchy.exe",
    "caffeine.exe",
    "CrashHandler.exe",
    "RuntimeBroker.exe"
]

   NotDisplayTimer(input("Set Work Brake Timer: "))

   for i in range(0, len(Apps)):
       Apps.insert(i, Apps[i])

   tasklist = subprocess.getoutput('tasklist')

   TaskNames = tasklist.splitlines()[3:]

   for i in TaskNames[3:]:
       Task = i.split()[0]

       if Task in Apps: os.system(f'taskkill /F /IM "{Task}"')

Break()
win = Tk()
win.title("Brake")
win.geometry(f"{win.winfo_screenwidth()}x{win.winfo_screenheight()}")
win.resizable(False, False)
label = Label(win, text="Brake", font={"arial", 30, "Black"})
label.pack(expend=True)
win.mainloop()
