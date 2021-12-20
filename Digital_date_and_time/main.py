from tkinter import *
import time


# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/


def my_watch():
    x = time.strftime("Current date and time : \n%Y-%m-%d %H:%M:%S")
    clock.config(text=x)
    clock.after(200,my_watch)

root = Tk()
root.title("Digital_Date_And_Time")
root.geometry("700x200")
clock = Label(root, font = ("times", 50, "bold"), bg="white")
clock.grid(row=0, column=1)

Label_1=Label(root, bg='white', text="</Developed By:-Shailendra Singh/> \n DM me for further querry: https://www.instagram.com/python_Coderz_/", font=("bold",8), padx= 160)
Label_1.place(x=5,y=155)
my_watch()
root.mainloop()