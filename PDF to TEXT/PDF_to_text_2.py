import tkinter as tk
import PyPDF2
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
import pathlib




# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/



window=tk.Tk()
window.title("PDF to text converter")

def openfile():
    file=askopenfile(filetypes=[('PDF Files','*.pdf')])
    pdf_file=open(file.name,'rb')
    read_pdf=PyPDF2.PdfFileReader(pdf_file)
    no_of_pages=read_pdf.getNumPages()
    page=read_pdf.getPage(0)
    page_content=page.extractText()
    pathlib.Path('context.txt').write_text(page_content)
    showinfo("Done","Successfully Converted")
    
label=tk.Label(window,text="choose file: ")
label.grid(row=0,column=0,padx=5,pady=5)
python_coderz_=tk.Label(window,text="Follow @python_coderz_ at insta")
python_coderz_.grid(row=1,column=0, columnspan=2)

button=ttk.Button(window,text="Select",width=30,command=openfile)
button.grid(row=0,column=1,padx=5,pady=5)

window.mainloop()