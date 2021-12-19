import tkinter
from PIL import Image, ImageTk
import random
# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/


# top level widget which represents the main window of an application
root = tkinter.Tk()
root.geometry('300x300')
root.configure(bg='#ffeaa7')
root.title('Roll the Dice')
root.iconbitmap("dice.ico")

# adding label with different font and formatting
l1 = tkinter.Label(root, text="Hello Python Lovers", fg = "black",
        font = "Helvetica 16 bold italic",bg='#ffeaa7')
l1.pack()
l2 = tkinter.Label(root, text="Follow Python_Coderz_ at Instagram", fg = "black",
        font = "Helvetica 7 bold italic",bg='#ffeaa7')
l2.pack()

# images
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
# simulating the dice with random numbers between 0 to 6 and generating image
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
label1 = tkinter.Label(root, image=image1)
label1.image = image1
# packing a widget in the parent widget 
label1.pack(expand=True)

# function activated by button
def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    label1.configure(image=image1)
    # keep a reference
    label1.image = image1

# adding button, and command will use rolling_dice function
start_button= tkinter.Button(root, text="Roll the Dice", width=20, fg="black", bg="pink", bd=0, padx=20, pady=10, command=rolling_dice)
start_button.pack()
# call the mainloop of Tk
root.mainloop()

