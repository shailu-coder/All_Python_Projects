import tkinter as tk
from tkinter import ttk
from tkinter import *
import random, os
from tkinter import messagebox

# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/

billingapplication = Tk()
billingapplication.geometry("1000x545")
billingapplication.title("Billing Software - Python_Coderz_")
billingapplication.iconbitmap("icon.ico")
billingapplication.resizable(0, 0)

#***************** Billing Software Main Title ******************

billingsoftwareframe = LabelFrame(billingapplication)
billingsoftwareframe.pack(side = TOP, fill = X)

billingsoftwarelabel = Label(billingsoftwareframe, text = "Billing Software", bd = 12, relief = GROOVE, bg = "#074463", fg = "yellow", font = ('Times New Roman', 16, 'bold'))
billingsoftwarelabel.pack(pady = 2, fill = X)

#****************************** END ******************************

#****************************** Variables ************************
#************ Customer Variables *************

custname = StringVar()
custcontno = StringVar()
custbillno = StringVar()
custbillno.set(str(random.randint(10000, 99999)))
searchbill = StringVar()

#****************** END **********************

#********** Cosmetics **********

soap = IntVar()
facecream = IntVar()
facewash = IntVar()
hairspray = IntVar()
hairgel = IntVar()
bodylotion = IntVar()

#*********** END ****************

#************ Grocery ***********

rice = IntVar()
edibleoil = IntVar()
daal = IntVar()
wheat = IntVar()
sugar = IntVar()
tea = IntVar()

#*************** END ************

#************ Cold Drink ********

cocacola = IntVar()
pepsi = IntVar()
mirinda = IntVar()
fanta = IntVar()
sprite = IntVar()
frooti = IntVar()

#*************** END ************

#************** Total Bill Area *************

totalcosmeticprice = IntVar()
totalgroceryprice = IntVar()
totalcolddrinkprice = IntVar()
cosmetictax = IntVar()
grocerytax = IntVar()
colddrinktax = IntVar()

#********************* END *******************

#********************************* END ***************************

#************************ Functionalities ***********************

def total():
    totalcosmtprice = soap.get() * 39 + facecream.get() * 49 + facewash.get() * 69 + hairspray.get() * 99 + hairgel.get() * 149 + bodylotion.get() * 199
    totalgrocyprice = rice.get() * 49 + edibleoil.get() * 119 + daal.get() * 89 + wheat.get() * 79 + sugar.get() * 39 + tea.get() * 99
    totalcolddrnkprice = cocacola.get() * 29 + pepsi.get() * 29 + mirinda.get() * 39 + fanta.get() * 39 + sprite.get() * 29 + frooti.get() * 19

    totalcosmeticprice.set(totalcosmtprice)
    totalgroceryprice.set(totalgrocyprice)
    totalcolddrinkprice.set(totalcolddrnkprice)

    cosmetictax.set(round(totalcosmtprice * 0.18))
    grocerytax.set(round(totalgrocyprice * 0.05))
    colddrinktax.set(round(totalcolddrnkprice * 0.28))

def welcomebill():
    txtarea.delete("1.0", END)
    txtarea.insert(END, "      Welcome SMart Retail")

def customerdetails():
    txtarea.delete(1.0, END)
    txtarea.insert(END, "      Welcome SMart Retail")
    txtarea.insert(END, f"\nBill No : {custbillno.get()}")
    txtarea.insert(END, f"\nCust Name : {custname.get()}")
    txtarea.insert(END, f"\nCust Cont No : +91{custcontno.get()}")
    txtarea.insert(END, "\n*****************************")
    txtarea.insert(END, f"\nProducts\t  Quantity\t  Price")
    txtarea.insert(END, "\n*****************************")

def billamount():
    if(custname.get() == "") or (custcontno.get() == ""):
        messagebox.showerror("Billing Software", "Customer Details not present. Please check again.")
    
    elif(totalcosmeticprice.get() == 0) and (totalgroceryprice.get() == 0) and (totalcolddrinkprice.get() == 0):
        messagebox.showerror("Billing Software", "No Products are selected. Please check again.")
    
    else:
        customerdetails()
        if(soap.get() > 0):
            txtarea.insert(END, f"\nBath Soap\t\t{soap.get()}\t{soap.get() * 39}")

        if(facecream.get() > 0):
            txtarea.insert(END, f"\nFace Cream\t\t{facecream.get()}\t{facecream.get() * 49}")

        if(facewash.get() > 0):
            txtarea.insert(END, f"\nFace Wash\t\t{facewash.get()}\t{facewash.get() * 69}")
        
        if(hairspray.get() > 0):
            txtarea.insert(END, f"\nHair Spray\t\t{hairspray.get()}\t{hairspray.get() * 99}")

        if(hairgel.get() > 0):
            txtarea.insert(END, f"\nHair Gel\t\t{hairgel.get()}\t{hairgel.get() * 149}")
        
        if(bodylotion.get() > 0):
            txtarea.insert(END, f"\nBody Lotion\t\t{bodylotion.get()}\t{bodylotion.get() * 199}")

        
        if(rice.get() > 0):
            txtarea.insert(END, f"\nRice\t\t{rice.get()}\t{rice.get() * 49}")
        
        if(edibleoil.get() > 0):
            txtarea.insert(END, f"\nEdible Oil\t\t{edibleoil.get()}\t{edibleoil.get() * 119}")

        if(daal.get() > 0):
            txtarea.insert(END, f"\nDaal\t\t{daal.get()}\t{daal.get() * 89}")
        
        if(wheat.get() > 0):
            txtarea.insert(END, f"\nWheat\t\t{wheat.get()}\t{wheat.get() * 79}")
        
        if(sugar.get() > 0):
            txtarea.insert(END, f"\nSugar\t\t{sugar.get()}\t{sugar.get() * 39}")
        
        if(tea.get() > 0):
            txtarea.insert(END, f"\nTea\t\t{tea.get()}\t{tea.get() * 99}")

        
        if(cocacola.get() > 0):
            txtarea.insert(END, f"\nCocacola\t\t{cocacola.get()}\t{cocacola.get() * 29}")
        
        if(pepsi.get() > 0):
            txtarea.insert(END, f"\nPepsi\t\t{pepsi.get()}\t{pepsi.get() * 29}")
        
        if(mirinda.get() > 0):
            txtarea.insert(END, f"\nMirinda\t\t{mirinda.get()}\t{mirinda.get() * 39}")
        
        if(fanta.get() > 0):
            txtarea.insert(END, f"\nFanta\t\t{fanta.get()}\t{fanta.get() * 39}")
        
        if(sprite.get() > 0):
            txtarea.insert(END, f"\nsprite\t\t{sprite.get()}\t{sprite.get() * 29}")
        
        if(frooti.get() > 0):
            txtarea.insert(END, f"\nFrooti\t\t{frooti.get()}\t{frooti.get() * 19}")
        
        txtarea.insert(END, "\n----------------------------")

        if(cosmetictax.get() > 0):
            txtarea.insert(END, f"\nCosmetic Tax\t\t\t{cosmetictax.get()}")
        
        if(grocerytax.get() > 0):
            txtarea.insert(END, f"\nGrocery Tax\t\t\t{grocerytax.get()}")
        
        if(colddrinktax.get() > 0):
            txtarea.insert(END, f"\nCold Drink Tax\t\t\t{colddrinktax.get()}")

        txtarea.insert(END, "\n----------------------------")

        txtarea.insert(END, f"\nTotal\t\t\t{totalcosmeticprice.get() + totalgroceryprice.get() + totalcolddrinkprice.get() + cosmetictax.get() + grocerytax.get() + colddrinktax.get()}")

        savebill()

def savebill():
    save = messagebox.askyesno("Billing Software", "Do you want to save the bill?")

    if(save > 0):
        billdata = txtarea.get(1.0, END)
        with open(f'Customer Bills/{custbillno.get()}.txt', "w") as wf:
            wf.write(billdata)
        
        messagebox.showinfo("Billing Software", f"{custbillno.get()}.txt" + " saved successfully.")
    
    else:
        return

def findbill():
    found = "No"
    
    for i in os.listdir("Customer Bills/"):
        if i.split(".")[0] == searchbill.get():
            with open(f'Customer Bills/{i}', "r") as rf:
                txtarea.delete("1.0", END)
                for d in rf:
                    txtarea.insert(END, d) 
            found = "yes"

    if(found == "no"):
        messagebox.showerror("Billing Software", "Invalid Bill No.")    

def clear():
    clearopt = messagebox.askyesno("Billing Software", "Do you really want to clear?")
    if(clearopt > 0):
#************ Customer Variables *************

        custname.set("")
        custcontno.set("")
        custbillno.set("")
        searchbill.set("")

    #****************** END **********************

    #********** Cosmetics **********

        soap.set(0)
        facecream.set(0)
        facewash.set(0)
        hairspray.set(0)
        hairgel.set(0)
        bodylotion.set(0)

    #*********** END ****************

    #************ Grocery ***********

        rice.set(0)
        edibleoil.set(0)
        daal.set(0)
        wheat.set(0)
        sugar.set(0)
        tea.set(0)

    #*************** END ************

    #************ Cold Drink ********

        cocacola.set(0)
        pepsi.set(0)
        mirinda.set(0)
        fanta.set(0)
        sprite.set(0)
        frooti.set(0)

    #*************** END ************

    #************** Total Bill Area *************

        totalcosmeticprice.set(0)
        totalgroceryprice.set(0)
        totalcolddrinkprice.set(0)
        cosmetictax.set(0)
        grocerytax.set(0)
        colddrinktax.set(0)

    #********************* END *******************
        welcomebill()
    
    else:
        return

def exitopt():
    exitop = messagebox.askyesno("Billing Software", "Do you really want to exit?")

    if(exitop > 0):
        billingapplication.destroy()

    else:
        return


#****************************** END *****************************

#****************** Customer Details Frame ***********************

billingcustomerframe = LabelFrame(billingapplication, text = "Customer Details", bd = 12, relief = GROOVE, bg = "#074463", fg = "yellow", font = ('Times New Roman', 12, 'bold'))
billingcustomerframe.pack(side = TOP, fill = X)

custnamelabel = Label(billingcustomerframe, text = "Customer Name", bg = "#074463", fg = "white", font = ('Times New Roman', 12, 'bold'))
custnamelabel.pack(side = LEFT, padx = 20)

custnameentry = Entry(billingcustomerframe, textvariable = custname, width = 20, bd = 5, relief = SUNKEN)
custnameentry.pack(side = LEFT, padx = 5)

custcontnolabel = Label(billingcustomerframe, text = "Contact No.", bg = "#074463", fg = "white", font = ('Times New Roman', 12, 'bold'))
custcontnolabel.pack(side = LEFT, padx = 20)

countrycodeentry = Entry(billingcustomerframe, width = 4, bd = 5, relief = SUNKEN)
countrycodeentry.pack(side = LEFT, padx = 5)

countrycodeentry.insert(0, "+91")

custcontnoentry = Entry(billingcustomerframe, textvariable = custcontno, width = 15, bd = 5, relief = SUNKEN)
custcontnoentry.pack(side = LEFT, padx = 2)

custbillnolabel = Label(billingcustomerframe, text = "Bill Number", bg = "#074463", fg = "white", font = ('Times New Roman', 12, 'bold'))
custbillnolabel.pack(side = LEFT, padx = 20)

custbillnoentry = Entry(billingcustomerframe, textvariable = searchbill, width = 20, bd = 5, relief = SUNKEN)
custbillnoentry.pack(side = LEFT, padx = 5)

custsearchbtn = Button(billingcustomerframe, text = "Search", bd = 5, relief = GROOVE, bg = "white", fg = "black", font = ('Times New Roman', 12, 'bold'), command = findbill)
custsearchbtn.pack(side = LEFT, padx = 20)

#********************************** END **************************

#************************ Cosmetics Frame ************************

cosmeticsframe = LabelFrame(billingapplication, text = "Cosmetics", bd = 12, relief = GROOVE, bg = "#074463", fg = "yellow", font = ('Times New Roman', 12, 'bold'))
cosmeticsframe.place(x = 0, y = 132, width = 250, height = 260)

bathsoaplabel = Label(cosmeticsframe, text = "Bath Soap", bg = "#074463", fg = "#00FFD4", font = ('Times New Roman', 12, 'bold'))
bathsoaplabel.grid(row = 0, column = 0, padx = 2, pady = 5)

bathsoapentry = Entry(cosmeticsframe, textvariable = soap, width = 10, bd = 5, relief = SUNKEN)
bathsoapentry.grid(row = 0, column = 1, padx = 5, pady = 5)

facecreamlabel = Label(cosmeticsframe, text = "Face Cream", bg = "#074463", fg = "#00FFD4", font = ('Times New Roman', 12, 'bold'))
facecreamlabel.grid(row = 1, column = 0, padx = 2, pady = 5)

facecreamentry = Entry(cosmeticsframe, textvariable = facecream, width = 10, bd = 5, relief = SUNKEN)
facecreamentry.grid(row = 1, column = 1, padx = 5, pady = 5)

facecreamlabel = Label(cosmeticsframe, text = "Face Wash", bg = "#074463", fg = "#00FFD4", font = ('Times New Roman', 12, 'bold'))
facecreamlabel.grid(row = 2, column = 0, padx = 2, pady = 5)

facewashentry = Entry(cosmeticsframe, textvariable = facewash, width = 10, bd = 5, relief = SUNKEN)
facewashentry.grid(row = 2, column = 1, padx = 5, pady = 5)

hairspraylabel = Label(cosmeticsframe, text = "Hair Spray", bg = "#074463", fg = "#00FFD4", font = ('Times New Roman', 12, 'bold'))
hairspraylabel.grid(row = 3, column = 0, padx = 2, pady = 2)

hairsprayentry = Entry(cosmeticsframe, textvariable = hairspray, width = 10, bd = 5, relief = SUNKEN)
hairsprayentry.grid(row = 3, column = 1, padx = 5, pady = 5)

hairgellabel = Label(cosmeticsframe, text = "Hair Gel", bg = "#074463", fg = "#00FFD4", font = ('Times New Roman', 12, 'bold'))
hairgellabel.grid(row = 4, column = 0, padx = 2, pady = 5)

hairgelentry = Entry(cosmeticsframe, textvariable = hairgel, width = 10, bd = 5, relief = SUNKEN)
hairgelentry.grid(row = 4, column = 1, padx = 5, pady = 5)

bodylotionlabel = Label(cosmeticsframe, text = "Body Lotion", bg = "#074463", fg = "#00FFD4", font = ('Times New Roman', 12, 'bold'))
bodylotionlabel.grid(row = 5, column = 0, padx = 2, pady = 5)

bodylotionentry = Entry(cosmeticsframe, textvariable = bodylotion, width = 10, bd = 5, relief = SUNKEN)
bodylotionentry.grid(row = 5, column = 1, padx = 5, pady = 5)

#**************************** END **********************************

#************************ Grocey Frame *****************************

groceryframe = LabelFrame(billingapplication, text = "Grocery", bd = 12, relief = GROOVE, bg = "#074463", fg = "yellow", font = ('Times New Roman', 12, 'bold'))
groceryframe.place(x = 252, y = 132, width = 230, height = 260)

ricelabel = Label(groceryframe, text = "Rice", bg = "#074463", fg = "#00FFD4", font = ('Times New Roman', 12, 'bold'))
ricelabel.grid(row = 0, column = 0, padx = 2, pady = 5)

riceentry = Entry(groceryframe, textvariable = rice, width = 10, bd = 5, relief = SUNKEN)
riceentry.grid(row = 0, column = 1, padx = 5, pady = 5)

edibleoillabel = Label(groceryframe, text = "Edible Oil", bg = "#074463", fg = "#00FFD4", font = ('Times New Roman', 12, 'bold'))
edibleoillabel.grid(row = 1, column = 0, padx = 2, pady = 5)

edibleoilentry = Entry(groceryframe, textvariable = edibleoil, width = 10, bd = 5, relief = SUNKEN)
edibleoilentry.grid(row = 1, column = 1, padx = 5, pady = 5)

daallabel = Label(groceryframe, text = "Daal", bg = "#074463", fg = "#00FFD4", font = ('Times New Roman', 12, 'bold'))
daallabel.grid(row = 2, column = 0, padx = 2, pady = 5)

daalentry = Entry(groceryframe, textvariable = daal, width = 10, bd = 5, relief = SUNKEN)
daalentry.grid(row = 2, column = 1, padx = 5, pady = 5)

wheatlabel = Label(groceryframe, text = "Wheat", bg = "#074463", fg = "#00FFD4", font = ('Times New Roman', 12, 'bold'))
wheatlabel.grid(row = 3, column = 0, padx = 2, pady = 5)

wheatentry = Entry(groceryframe, textvariable = wheat, width = 10, bd = 5, relief = SUNKEN)
wheatentry.grid(row = 3, column = 1, padx = 5, pady = 5)

sugarlabel = Label(groceryframe, text = "Sugar", bg = "#074463", fg = "#00FFD4", font = ('Times New Roman', 12, 'bold'))
sugarlabel.grid(row = 4, column = 0, padx = 2, pady = 5)

sugarentry = Entry(groceryframe, textvariable = sugar, width = 10, bd = 5, relief = SUNKEN)
sugarentry.grid(row = 4, column = 1, padx = 5, pady = 5)

tealabel = Label(groceryframe, text = "Tea", bg = "#074463", fg = "#00FFD4", font = ('Times New Roman', 12, 'bold'))
tealabel.grid(row = 5, column = 0, padx = 2, pady = 5)

teaentry = Entry(groceryframe, textvariable = tea, width = 10, bd = 5, relief = SUNKEN)
teaentry.grid(row = 5, column = 1, padx = 5, pady = 5)

#******************************* END **********************************

#*************************** Cold Drink Frame *************************

colddrinkframe = LabelFrame(billingapplication, text = "Cold Drink", bd = 12, relief = GROOVE, bg = "#074463", fg = "yellow", font = ('Times New Roman', 12, 'bold'))
colddrinkframe.place(x = 484, y = 132, width = 230, height = 260)

cocacolalabel = Label(colddrinkframe, text = "Coca Cola", bg = "#074463", fg = "#00FFD4", font = ('Times New Roman', 12, 'bold'))
cocacolalabel.grid(row = 0, column = 0, padx= 2, pady = 5)

cocacolaentry = Entry(colddrinkframe, textvariable = cocacola, width = 10, bd = 5, relief = SUNKEN)
cocacolaentry.grid(row = 0, column  = 1, padx = 5, pady = 5)

pepsilabel = Label(colddrinkframe, text = "Pepsi", bg = "#074463", fg = "#00FFD4", font = ('Times New Roman', 12, 'bold'))
pepsilabel.grid(row = 1, column = 0, padx= 2, pady = 5)

pepsientry = Entry(colddrinkframe, textvariable = pepsi, width = 10, bd = 5, relief = SUNKEN)
pepsientry.grid(row = 1, column  = 1, padx = 5, pady = 5)

mirindaalabel = Label(colddrinkframe, text = "Mirinda", bg = "#074463", fg = "#00FFD4", font = ('Times New Roman', 12, 'bold'))
mirindaalabel.grid(row = 2, column = 0, padx= 2, pady = 5)

mirindaaentry = Entry(colddrinkframe, textvariable = mirinda, width = 10, bd = 5, relief = SUNKEN)
mirindaaentry.grid(row = 2, column  = 1, padx = 5, pady = 5)

fantalabel = Label(colddrinkframe, text = "Fanta", bg = "#074463", fg = "#00FFD4", font = ('Times New Roman', 12, 'bold'))
fantalabel.grid(row = 3, column = 0, padx= 2, pady = 5)

fantaentry = Entry(colddrinkframe, textvariable = fanta, width = 10, bd = 5, relief = SUNKEN)
fantaentry.grid(row = 3, column  = 1, padx = 5, pady = 5)

spritelabel = Label(colddrinkframe, text = "Sprite", bg = "#074463", fg = "#00FFD4", font = ('Times New Roman', 12, 'bold'))
spritelabel.grid(row = 4, column = 0, padx= 2, pady = 5)

spriteentry = Entry(colddrinkframe, textvariable = sprite, width = 10, bd = 5, relief = SUNKEN)
spriteentry.grid(row = 4, column  = 1, padx = 5, pady = 5)

frootilabel = Label(colddrinkframe, text = "Frooti", bg = "#074463", fg = "#00FFD4", font = ('Times New Roman', 12, 'bold'))
frootilabel.grid(row = 5, column = 0, padx= 2, pady = 5)

frootientry = Entry(colddrinkframe, textvariable = frooti, width = 10, bd = 5, relief = SUNKEN)
frootientry.grid(row = 5, column  = 1, padx = 5, pady = 5)

#******************************* END ************************************

#***************************** Bill Area Frame **************************

billareaframe = LabelFrame(billingapplication, bd = 10, relief = SUNKEN)
billareaframe.place(x = 716, y = 132, width = 274, height = 260)

billareatitle = Label(billareaframe, text = "Bill Area", bd = 5, relief = GROOVE, bg = "white", fg = "black", font = ('Times New Roman', 12, 'bold'))
billareatitle.pack(fill = X)

yscroll = Scrollbar(billareaframe, orient = VERTICAL)
txtarea = Text(billareaframe, yscrollcommand = yscroll.set)
yscroll.pack(side = RIGHT, fill = Y)
yscroll.config(command = txtarea.yview)
txtarea.pack(fill = BOTH, expand = True)

#******************************* END *******************************

#************************* Billing Menu Frame **********************

billingmenuframe = LabelFrame(billingapplication, text = "Billing Menu", bd = 12, relief = GROOVE, bg = "#074463", fg = "yellow", font = ('Times New Roman', 12, 'bold'))
billingmenuframe.place(x = 0, y = 394, width = 600, height = 150)

totalcosmeticpricelabel = Label(billingmenuframe, text = "Total Cosmetic Price", bg = "#074463", fg = "white", font = ('Times new Roman', 12, 'bold'))
totalcosmeticpricelabel.grid(row = 0, column  = 0, padx = 2, pady = 5)

totalcosmeticpriceentry = Entry(billingmenuframe, textvariable = totalcosmeticprice, width = 10, bd = 5, relief = SUNKEN)
totalcosmeticpriceentry.grid(row = 0, column = 1, padx = 5, pady = 5)

cosmetictaxlabel = Label(billingmenuframe, text = "Cosmetic Tax", bg = "#074463", fg = "white", font = ('Times new Roman', 12, 'bold'))
cosmetictaxlabel.grid(row = 0, column = 2, padx = 20, pady = 5)

cosmetictaxentry = Entry(billingmenuframe, textvariable = cosmetictax, width = 10, bd = 5, relief = SUNKEN)
cosmetictaxentry.grid(row = 0, column = 3, padx = 5, pady = 5)

totalgrocerypricelabel = Label(billingmenuframe, text = "Total Grocery Price", bg = "#074463", fg = "white", font = ('Times new Roman', 12, 'bold'))
totalgrocerypricelabel.grid(row = 1, column  = 0, padx = 2, pady = 5)

totalgrocerypriceentry = Entry(billingmenuframe, textvariable = totalgroceryprice, width = 10, bd = 5, relief = SUNKEN)
totalgrocerypriceentry.grid(row = 1, column = 1, padx = 5, pady = 5)

grocerytaxlabel = Label(billingmenuframe, text = "Grocery Tax", bg = "#074463", fg = "white", font = ('Times new Roman', 12, 'bold'))
grocerytaxlabel.grid(row = 1, column = 2, padx = 20, pady = 5)

grocerytaxentry = Entry(billingmenuframe, textvariable = grocerytax, width = 10, bd = 5, relief = SUNKEN)
grocerytaxentry.grid(row = 1, column = 3, padx = 5, pady = 5)

totalcolddrinkpricelabel = Label(billingmenuframe, text = "Total Cold Drink Price", bg = "#074463", fg = "white", font = ('Times new Roman', 12, 'bold'))
totalcolddrinkpricelabel.grid(row = 2, column  = 0, padx = 2, pady = 5)

totalcolddrinkpriceentry = Entry(billingmenuframe, textvariable = totalcolddrinkprice, width = 10, bd = 5, relief = SUNKEN)
totalcolddrinkpriceentry.grid(row = 2, column = 1, padx = 5, pady = 5)

colddrinktaxlabel = Label(billingmenuframe, text = "Cold Drink Tax", bg = "#074463", fg = "white", font = ('Times new Roman', 12, 'bold'))
colddrinktaxlabel.grid(row = 2, column = 2, padx = 20, pady = 5)

colddrinktaxentry = Entry(billingmenuframe, textvariable = colddrinktax, width = 10, bd = 5, relief = SUNKEN)
colddrinktaxentry.grid(row = 2, column = 3, padx = 5, pady = 5)

butttonframe = LabelFrame(billingapplication, bd = 10, bg = "#074463", fg = "white", relief = GROOVE)
butttonframe.place(x = 602, y = 394, width = 398, height = 150)

totalbtn = Button(butttonframe, text = "Total", bg = "black", fg = "white", relief = SUNKEN, font = ('Times new Roman', 14, 'bold'), command = total)
totalbtn.grid(row = 0, column = 0, padx = 10, pady = 45)

generatebillbtn = Button(butttonframe, text = "Generate Bill", bg = "black", fg = "white", relief = SUNKEN, font = ('Times new Roman', 14, 'bold'), command = billamount)
generatebillbtn.grid(row = 0, column = 1, padx = 10, pady = 45)

clearbtn = Button(butttonframe, text = "Clear", bg = "black", fg = "white", relief = SUNKEN, font = ('Times new Roman', 14, 'bold'), command = clear)
clearbtn.grid(row = 0, column = 2, padx = 10, pady = 45)

exitbtn = Button(butttonframe, text = "Exit", bg = "black", fg = "white", relief = SUNKEN, font = ('Times new Roman', 14, 'bold'), command = exitopt)
exitbtn.grid(row = 0, column = 3, padx = 10, pady = 45)

welcomebill()

billingapplication.mainloop()