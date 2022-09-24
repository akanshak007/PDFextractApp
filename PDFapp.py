from operator import truediv
import tkinter as tk
import PyPDF2
from PIL import Image,  ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()
canvas = tk.Canvas(root, width=1200, height=600)
canvas.grid(columnspan=3, rowspan=3)


#logo
logo = Image.open('C:\mygit\TextExtractionAPP\PDFextractApp\logo.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(root, text="Select a PDF file on your computer to extract its text", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

def open_file():
    browse_text.set("loading..")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetype=[("Pdf file","*.pdf")])
    if file:
        #print("File loaded successfuly!")
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        
        #text box
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height= 2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)





root.mainloop()


