import tkinter as tk
import PyPDF2
from PIL import Image,  ImageTk

root = tk.Tk()
canvas = tk.Canvas(root, width=1200, height=600)
canvas.grid(columnspan=3)


#logo
logo = Image.open('logo.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instruction
#instruction = tk.Label(root, "Select a PDF file on your computer to extract its text", font="Raleway")
#instruction.grid(columnspan=3, column=0, row=1)

root.mainloop()


