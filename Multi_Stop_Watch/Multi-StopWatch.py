# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/

import tkinter as tk
import time

class digitalclock(tk.Frame):
    def __init__(self, master=None, **kwords):
        super().__init__(master, **kwords)
        top = tk.Frame(self)
        top.pack()
        buttons = ("Start Stop Reset Quit")
        for butn in buttons.split():
            setattr(self, butn, butn)
            action = lambda act=butn: self.showtime(act)
            tk.Button(top, text=butn, command=action).pack(side="left")
        self.lab = tk.Label(self, text="00:00:00", bg=self.cget("bg"))
        self.lab.pack(side="bottom")
        self.showtime(self.Reset)

    def showtime(self, *args):
        if args:
            act = args[0]
            if act == self.Quit:
                self.run = False
                self.quit()
            elif act == self.Reset:
                self.elapsed = 0.0
                self.run = False
                self.lab.config(text = "00:00:00")
            elif act == self.Start and self.run == False:
                self.starttime = time.time() - self.elapsed
                self.run = True
            elif act == self.Stop and self.run == True:
                self.elapsed = time.time() - self.starttime
                self.run = False
        if self.run == True:
            tim = int(time.time() - self.starttime)
            hms = (tim // 3600, tim % 3600 // 60, tim % 60)
            self.lab.config(text = '{:02d}:{:02d}:{:02d}'.format(*hms))
            self.after(200,self.showtime)

root=tk.Tk()
root.title("Multi_Stopwatch")
colr = ["sky blue", "orange", "lightgreen", "yellow", "orchid1", "bisque2"]
[digitalclock(root, bd=8, bg=c).pack() for c in colr]
root.mainloop()
