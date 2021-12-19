
from tkinter import *
from speedtest import Speedtest
import webbrowser

# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/

def check_speed():
    speed_test = Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()
    download_speed = round(download/(10**6),2)
    upload_speed = round(upload/(10**6),2)
    down_label.config(text="Download Speed - "+ str(download_speed)+" Mbps")
    up_label.config(text="Upload Speed - "+ str(upload_speed)+" Mbps")


def open_site():
    webbrowser.open("https://www.instagram.com/python_coderz_/")

#check_speed()

root = Tk()
root.title("INTERNET SPEEDTEST")
root.geometry('300x400')
root.config(bg='black')
root.resizable(False,False)

canvas = Canvas(root, width = 300, height = 400,bg="black")      
canvas.pack()      

button = Button(root,text="GET SPEED",width=10,command=check_speed)
button.place(x=110,y=345)
down_label = Label(root,text="",width=25)
down_label.place(x=60,y=275)
up_label = Label(root,text="",width=25)
up_label.place(x=60,y=307)

followus = Label(root, text ='Click To Follow Us At Insta', bg='#fff', fg='#404042', font = 'arial 10 bold')
followus.place(x=70,y=80)

python_coderz_ = Button(root, text ='@Python_Coderz_', bg='#fff', fg='#404042', font = 'arial 15 bold', command=open_site)
python_coderz_.place(x=60,y=107)

root.mainloop()
