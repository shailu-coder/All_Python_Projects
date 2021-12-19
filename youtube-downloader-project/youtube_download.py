from pytube import YouTube
import os
from tkinter import *

# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/

root=Tk()
root.geometry('600x200')
root.title('Youtube Video Downloader')


Label_1=Label(root,text="Paste The Youtube Link Here", font=("bold",20))
Label_1.place(x=120,y=20)

Label_2=Label(root, text="</Developed By:-Shailendra Singh/> \n DM me for further querry: https://www.instagram.com/python_coderz_/", font=("bold",9))
Label_2.place(x=140,y=150)

mylink=StringVar()

pastelink=Entry(root, width=60, textvariable=mylink)
pastelink.place(x=140, y=80)

def downloadVideo():
    x=str(mylink.get())

    if not os.path.exists('./downlaoded_video'):
        os.makedirs('./downlaoded_video')
    ytvideo=YouTube(x)
    stream=ytvideo.streams.all()
    for i in stream:
        print(i)

    ytvideo.streams.last().download('./downlaoded_video')




Button(root,text="Download Video", width=20, bg='green',fg="white", command=downloadVideo).place(x=220, y=110)

root.mainloop()