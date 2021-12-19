from tkinter import *
from tkinter import ttk
# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/


converter = Tk()
converter.geometry("600x410") #to define size of the box

converter.title("Currency Converter") #title of app
# converter.wm_iconbitmap("1.ico")    #icon of app

#dictionary of currency of different countries
OPTIONS = {
    "Australian Dollar":53.62,
    "Brazilian Real":14.10,
    "British Pound":98.05,
    "Bulgarian Lev":45.23,
    "Chinese Yaun":10.7,
    "Euro":88.49,
    "HongKong Dollor":9.68,
    "Indonesian Rupiah":0.0051,
    "Japenese Yen":0.71,
    "Pakistani Rupee":0.45,
    "SriLankan Rupee":0.41,
    "Swiss Franc":82.03,
    "US Dollar":75.02
    }

# function to convert them into different currencies
def ok():
    price = rupees.get()
    answer = var.get()
    DICT = OPTIONS.get(answer,None)
    converted = float(DICT)*float(price)
    result.delete(1.0,END)
    result.insert(INSERT,"Price in ",INSERT,answer,INSERT," = ",
                  INSERT,converted)







    
# heading of app
appName = Label(converter,text="Currency Converter",
                font=("arial",25,"bold","underline"),fg="dark blue")

appName.grid(row=0,column=1)

#textbox to display the result
result= Text(converter,height=5,width=50,font=("arial",10,"bold"),bd=5)
result.grid(row=1,column=1,columnspan=10,pady=20)

# label for indian rupees
india = Label(converter,text="Indian Rupees : ",
              font=("arial",10,"bold"),fg="blue")
india.grid(row=2,column=0,pady=20)

#text box of rupees
rupees = Entry(converter,font=("calibri",20))
rupees.grid(row=2,column=1,pady=20)

#label for choice country
choice = Label(converter,text="Choice Country : ",
              font=("arial",10,"bold"),fg="blue")
choice.grid(row=3,column=0)

#drop downlist
var = StringVar(converter)
var.set(None)
option = OptionMenu(converter,var,*OPTIONS)
option.grid(row=3,column=1,sticky="ew")

#button to convert them into different currencies
button = Button(converter,text="Convert",
                fg="blue",font=("calibri",20),bg="powder blue",command=ok)
button.grid(row=4,column=1,pady=20)


pythonlabel = Label(converter,text="Follow Python_Coderz_ On Instagram For Amazing Projects! ",
              font=("arial",10,"bold"),fg="#e17055")
pythonlabel.grid(row=5,column=0, columnspan=4, padx=60)

mainloop()





















