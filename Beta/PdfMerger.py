from tkinter.filedialog import askopenfilename, asksaveasfilename
import PyPDF2
from Utility import pdfMerger

from customtkinter import *

filePath = ""
finalFileLoc = ""

pdfFiles = []

def addPDfFiles():

    global filePath

    filePath = askopenfilename(title = "Select PDf file",
                           filetypes = [("PDF Files", "*.pdf")])

    pdfFiles.append(filePath)

def FinalFileLoc():

    global finalFileLoc

    finalFileLoc =  str(asksaveasfilename(defaultextension = ".pdf"))

app = CTk()
app.title('PDF File Merger')
app.geometry("800x600")
app.resizable(False, False)

addFile = CTkButton(
	app,
	text = "Add PDF File",
	font = ("Calibre", 14),
	command = addPDfFiles,
	width = 100
)

addFile.place(x = 20, y = 20)

finalFileLocation = CTkButton(
	app,
	text = "Set File",
    font = ("Calibre", 14),
	command = FinalFileLoc,
	width = 100
)

finalFileLocation.place(x = 300, y = 20)

Merge = CTkButton(
	app,
	text = "Merge",
    font = ("Calibre", 14),
	command = lambda: pdfMerger(pdfFiles, finalFileLoc),
	width = 100
)

Merge.place(x = 150, y = 200)

app.mainloop()