import qrcode
from customtkinter import *

def generate_QRcode():
	qr = qrcode.QRCode(box_size = 10, border = 1)
	qr.add_data(url.get())
	img = qr.make_image(fill_color = "black", back_color = "white").convert("RGB")

	qrcode_ = CTkImage(light_image = img, dark_image = img, size = (100, 100))

	qrcode_display = CTkLabel(win, image = qrcode_, font = ("Console", 20), text = "")

	qrcode_display.configure(image = qrcode_)
	qrcode_display.place(x = 20, y = 100)

win = CTk()
win.title("QR Code Generator")
win.geometry("600x400")

url = CTkEntry(win, placeholder_text = "Enter URL", text_color = "white", width = 300)
url.place(x = 20, y = 30)

generate = CTkButton(win, text = "Generate", font = ("Console", 16), width = len("Generate"), command = generate_QRcode)
generate.place(x = 340, y = 30)

win.mainloop()
