from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import Image

# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/
# Watch My Video For More Info About This Project- https://www.youtube.com/watch?v=WXHUGYu5oag
root=Tk()
root.geometry("400x400")
root.title("Image_Conversion_App")


def jpg_to_png():
    filename=fd.askopenfilename()
    if filename.endswith(".jpg"):
        Image.open(filename).save("sample1.png")
    else:
        Label_2=Label(root,text="Error!", width=20,fg="red", font=("bold",15))
        Label_2.place(x=80,y=280)

def jpg_to_pdf():
    filename=fd.askopenfilename()
    if filename.endswith(".jpg"):
        Image.open(filename).save("sample1.pdf", resolution=100.0)
    else:
        Label_2=Label(root,text="Error!", width=20,fg="red", font=("bold",15))
        Label_2.place(x=80,y=280)

Label_1=Label(root,text="Browse A File", width=20, font=("bold",15))
Label_1.place(x=80,y=80)

Label_3=Label(root, text="</Developed By:-Shailendra Singh/> \n DM me for further querry:https://www.instagram.com/python_coderz_", font=("bold",8))
Label_3.place(x=10,y=365)




Button(root,text="JPG_to_PNG", width=20, height=2, bg="brown",fg="white",command=jpg_to_png).place(x=120,y=120)
Button(root,text="JPG_to_PDF", width=20, height=2, bg="brown",fg="white", command=jpg_to_pdf).place(x=120,y=220)

root.mainloop()