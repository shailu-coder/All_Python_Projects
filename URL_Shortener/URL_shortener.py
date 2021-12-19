import pyshorteners
import pyperclip
from tkinter import *

# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/



root =Tk()

root.title("URL shortener @Python_Coderz_")
root.config(bg="#49A")

url = StringVar()
url_address = StringVar()

def urlshortener():
    url_add=url.get()
    url_short=pyshorteners.Shortener().tinyurl.short(url_add)
    url_address.set(url_short)

def copyurl():
    url_short=url_address.get()
    pyperclip.copy(url_short)

Button(root, text="URL shortener " , bg='#4a536b', fg='#aed6dc',font="popins 20 bold" ).pack(pady=10)
Entry(root,textvariable=url ,width=50).pack(pady=5 )
Button(root, text="Generate short URL" , bg='#f0932b', fg='#aed6dc',font="popins 20 bold" ,command=urlshortener, ).pack(pady=7)
Entry(root,textvariable=url_address ,width=50).pack(pady=5)
Button(root, text="Copy URL" , bg='#6ab04c', fg='#aed6dc',font="popins 20 bold" ,command=copyurl).pack(pady=7)

root.mainloop()
