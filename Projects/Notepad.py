from tkinter.filedialog import askopenfilename, asksaveasfilename
from customtkinter import *
from tkinter import font

frame_open = False

filePath = ""

def OpenFile(writer):

    global filePath

    filePath = askopenfilename(title="Select A File", filetypes=[("Text Files", "*.txt")])

    if filePath:
        with open(filePath, "r") as f:
            content = f.read()
        writer.delete(1.0, END)
        writer.insert(END, content)
    return filePath

def writeToFile(writer):

    global filePath

    if filePath:
        content = writer.get(1.0, END).strip()

        with open(filePath, "w") as f:
            f.write(content)

def saveFileData(writer):

    global filePath

    filePath = asksaveasfilename(defaultextension = ".txt", filetypes=[("Text Files", "*.txt")]) + ".txt"

    if filePath:

         content = writer.get(1.0, END).strip()

         with open(filePath, 'w') as f:
            f.write(content)

def animate(widget, target_x, step=5, delay=7):
    current_x = widget.winfo_x()

    if current_x < target_x:
        new_x = min(current_x + step, target_x)
    else:
        new_x = max(current_x - step, target_x)

    widget.place(x=new_x, y=50)

    if new_x != target_x:
        widget.after(delay, lambda: animate(widget, target_x, step, delay))

def setFont(writer, name, size):

    if size == "": size = 20

    writer.configure(font = (name, int(size)))

def NotePad():
    global frame_open

    notepad = CTk()
    notepad.title("Notepad")
    notepad.geometry("600x300")

    notepad.grid_columnconfigure(0, weight=1)
    notepad.grid_rowconfigure(1, weight=1)

    writer = CTkTextbox(notepad, font = ("Arial", 20))
    writer.grid(row = 1, column = 0, sticky = "nsew", columnspan = 2)

    manage = CTkFrame(notepad, width=280, height=150)
    manage.place(x=-285, y=50)

    OpenFile_Display = CTkButton(manage, text="Open File", command=lambda: OpenFile(writer), height=35, width=75)
    OpenFile_Display.place(x=15, y=15)

    WriteData_Display = CTkButton(manage, text="Write Data", command=lambda: writeToFile(writer), height=35, width=75)
    WriteData_Display.place(x=100, y=15)

    available_fonts = list(font.families())
    available_fonts.sort()

    ChangeFont_label = CTkLabel(manage, text = "Font", font = ("Arial", 15))
    ChangeFont_label.place(x = 15, y = 70)

    ChangeFont = CTkComboBox(manage, values = available_fonts)
    ChangeFont.set("Arial")
    ChangeFont.place(x = 65, y = 70)

    ChangeSize = CTkEntry(manage, font = ("Arial", 15), placeholder_text = "size")
    ChangeSize.place(x = 65, y = 110)

    ChangeFont_button = CTkButton(
        manage, text = "Change Font",
        fg_color = "sea green",
        height = 35,
        width = 75,
        command = lambda: setFont(writer, ChangeFont.get(), ChangeSize.get()))

    ChangeFont_button.place(x = 185, y = 15)

    def toggleFrame():
        global frame_open
        if frame_open:
            animate(manage, -285)
        else:
            animate(manage, 5)
        frame_open = not frame_open

    openManage = CTkButton(notepad, text="Setting", font=("Arial", 15), width=15, command = toggleFrame)
    openManage.grid(row = 0, column = 1, sticky = "w", padx = 10, pady = 5)

    saveFile = CTkButton(notepad, text = "Save", font = ("Arial", 15), width = 15,fg_color = "green",
                         command = lambda: saveFileData(
        writer))
    saveFile.grid(row = 0, column = 0, sticky = "w", padx = 10, pady  =5)

    notepad.mainloop()

if __name__ == "__main__":
    NotePad()
