from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox 
from PIL import ImageTk, Image
import sqlite3

# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/

class userwindow:
    sqlite_var = 0 #variable to establish connection btw python and sqlite3
    theCursor = 0  #variable to store the indexing cursor   
    curItem=0 #variable to store currently active record
    
    def refresh(self):
        self.update_tree()
        self.clear_entries()
        print("Refreshed")
    
    def search_record(self):
        try:
            self.tree.delete(*self.tree.get_children())
            self.theCursor.execute("select * from Students where name like ? or phone like  ?",('%'+self.search_value.get()+'%','%'+self.search_value.get()+'%'))
            self.result = self.theCursor.fetchall()
            length=str(len(self.result))
            if(length==0):
                messagebox.showinfo("Search Results","No results were found, try again using part of name or phone no")
            if(length!='0'):
                i=0
                for row in self.result:
                    if(i%2==0):
                        self.tree.insert("",END, values=row,tag='1')
                    else:
                        self.tree.insert("",END, values=row,tag='2')  
                    i=i+1                    
        except:
            raise
            print("Couldn't search Data")


    def clear_entries(self):
        self.search_value.set("")
    
    def update_tree(self):
        try:
            self.tree.delete(*self.tree.get_children())
            self.theCursor.execute("SELECT * FROM Students")
            self.rows = self.theCursor.fetchall()
            i=0
            for row in self.rows:
                if(i%2==0):
                    self.tree.insert("",END, values=row,tag='1')
                else:
                    self.tree.insert("",END, values=row,tag='2')  
                i=i+1                    
        except:
            print("Couldn't Update Data")
    

    def setup_db(self):
        try:
            self.sqlite_var = sqlite3.connect('student.db')
            self.theCursor = self.sqlite_var.cursor()
        except:
            print("Could not establish connection to sqlite3")

        try:
            self.theCursor.execute("CREATE TABLE if not exists Students(ID INTEGER PRIMARY KEY AUTOINCREMENT , Name TEXT UNIQUE NOT NULL , Phone TEXT NOT NULL,Address TEXT NOT NULL);")
        except:
            print("ERROR : Table not created")
        finally:
            self.sqlite_var.commit()
            self.update_tree()

    def __init__(self):

        self.user_window=Tk()
        self.user_window.resizable(False, False)
        self.user_window.iconbitmap("logo.ico") 
        self.user_window.title("REGISTRX Database - User")



        # ----- 5th Row -----
        self.tree= ttk.Treeview(self.user_window,selectmode="browse",column=("column1", "column2", "column3","column4"), show='headings')
        self.tree.column("column1",width=100,minwidth=100,stretch=NO)
        self.tree.heading("#1", text="ADMISSION")
        self.tree.column("column2",width=180,minwidth=180,stretch=NO)
        self.tree.heading("#2", text="NAME")
        self.tree.column("column3",width=180,minwidth=180,stretch=NO)
        self.tree.heading("#3", text="PHONE")
        self.tree.column("column4",width=450,minwidth=450,stretch=NO)
        self.tree.heading("#4", text="ADDRESS")
        self.tree.tag_configure('1', background='ivory2')
        self.tree.tag_configure('2', background='alice blue')
        self.tree.grid(row=4,column=0,columnspan=4,sticky=W+E,padx=9,pady=9)
 
        Label(self.user_window,text="Search by Part of NAME or PHONE no").grid(row=5,column=0,columnspan=2,pady=9,padx=9,sticky=E)
        self.search_value = StringVar(self.user_window, value="")
        Entry(self.user_window,textvariable=self.search_value).grid(row=5,column=2,pady=9,padx=9,sticky=W+E)
        self.search_button = ttk.Button(self.user_window,text="Search",command=self.search_record)
        self.search_button.grid(row=5,column=3,pady=9,padx=9,sticky=W+E)
        
        self.refresh_button = ttk.Button(self.user_window,text="Refresh",command=self.refresh)
        self.refresh_button.grid(row=6, column=2,padx=9,pady=9,sticky=W+E)


        self.setup_db()
        self.user_window.mainloop()


class adminwindow:

    sqlite_var = 0 #variable to establish connection btw python and sqlite3
    theCursor = 0  #variable to store the indexing cursor   
    curItem=0 #variable to store currently active record
    
    def refresh(self):
        self.update_tree()
        self.clear_entries()
        print("Refreshed")

    def search_record(self):
        try:
            self.tree.delete(*self.tree.get_children())
            self.theCursor.execute("select * from Students where name like ? or phone like  ?",('%'+self.search_value.get()+'%','%'+self.search_value.get()+'%'))
            self.result = self.theCursor.fetchall()
            length=str(len(self.result))
            if(length==0):
                messagebox.showinfo("Search Results","No results were found, try again using part of name or phone no")
            if(length!='0'):
                i=0
                for row in self.result:
                    if(i%2==0):
                        self.tree.insert("",END, values=row,tag='1')
                    else:
                        self.tree.insert("",END, values=row,tag='2')  
                    i=i+1                    
        except:
            raise
            print("Couldn't search Data")

    def reset_db(self):
        yesno=messagebox.askquestion("RESET DB","All data in DB will be lost, continue ?")
        if(yesno=='yes'):
            self.theCursor.execute("DROP TABLE Students")
            print("Database Reseted")
            self.setup_db()
            self.update_tree()
     
    def clear_entries(self):
        self.Name_entry.delete(0, "end")
        self.Phone_no_entry.delete(0, "end")
        self.Address_entry.delete(0, "end")
    
    def delete_record(self):
        try:
            self.theCursor.execute("delete FROM Students WHERE ID=?",(self.curItem['values'][0],))     
            print("Deleted")
        except:
            print("Delete Failed !")
        finally:
            self.curItem=0
            self.clear_entries()                
            self.update_tree()
            self.sqlite_var.commit()

    def update_record(self):
        if(self.Name_value.get()!="" and self.Address_value.get()!="" and self.Phone_no_value.get()!=""):
            try:
                self.theCursor.execute("""UPDATE Students SET Name = ? ,Phone = ?,Address = ? WHERE ID= ? """,
                (self.Name_value.get(),self.Phone_no_value.get(),self.Address_value.get(),self.curItem['values'][0]))
                print("Update Records")
            except sqlite3.IntegrityError:
                messagebox.showerror("Duplicate","The Name already exists in the database")         
            except:
                print("Update Failed due to unkown reason !")
            finally:              
                self.update_tree()
                self.sqlite_var.commit()
        else:
            messagebox.showwarning("EMPTY INPUT","PLEASE FILL ALL REQUIRED DATA BEFORE UPDATING")

    def selectItem(self,event): 
        self.curItem = self.tree.item(self.tree.focus())
        print(self.curItem)
        self.Name_value.set(self.curItem["values"][1])
        self.Phone_no_value.set(self.curItem["values"][2])
        self.Address_value.set(self.curItem["values"][3])
   
    def update_tree(self):
        try:
            self.tree.delete(*self.tree.get_children())
            self.theCursor.execute("SELECT * FROM Students")
            self.rows = self.theCursor.fetchall()
            i=0
            for row in self.rows:
                if(i%2==0):
                    self.tree.insert("",END, values=row,tag='1')
                else:
                    self.tree.insert("",END, values=row,tag='2')  
                i=i+1                    
        except:
            print("Couldn't Update Data")
    
    def write_record(self):
        if(self.Name_value.get()!="" and self.Address_value.get()!="" and self.Phone_no_value.get()!=""):
            try:         
                self.theCursor.execute("""INSERT INTO Students (Name, Phone,Address) VALUES (?,?,?)""",
                (self.Name_value.get(),self.Phone_no_value.get(),self.Address_value.get()))
                self.sqlite_var.commit()
                self.theCursor.execute("SELECT *,max(id) FROM Students")
                self.rows=self.theCursor.fetchall()
                print(self.rows[0][0],"{Name : ",self.rows[0][1],"| No : ",self.rows[0][2],"| Address :",self.rows[0][3],"}  was ADDED ! ")
                self.clear_entries()
            except sqlite3.IntegrityError:
                messagebox.showerror("Duplicate","The Name already exists in the database")
            except:
                print("Data writing failed due to unknown reason")
            finally:
                self.update_tree()

        else:
            messagebox.showwarning("EMPTY INPUT","PLEASE FILL ALL REQUIRED DATA BEFORE SUBMITTING")


    def setup_db(self):
        try:
            self.sqlite_var = sqlite3.connect('student.db')
            self.theCursor = self.sqlite_var.cursor()
        except:
            print("Could not establish connection to sqlite3")

        try:
            self.theCursor.execute("CREATE TABLE if not exists Students(ID INTEGER PRIMARY KEY AUTOINCREMENT , Name TEXT UNIQUE NOT NULL , Phone TEXT NOT NULL,Address TEXT NOT NULL);")
        except:
            print("ERROR : Table not created")
        finally:
            self.sqlite_var.commit()
            self.update_tree()

    def __init__(self):

        self.admin_window=Tk()
        self.admin_window.resizable(False, False)
        self.admin_window.iconbitmap("logo.ico") 
        self.admin_window.title("REGISTRX Database - admin")

        # ----- 1st Row -----
        self.Name_Label = Label(self.admin_window, text="Name")
        self.Name_Label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        # Will hold the changing value stored first name
        self.Name_value = StringVar(self.admin_window, value="")
        self.Name_entry = ttk.Entry(self.admin_window,textvariable=self.Name_value)
        self.Name_entry.grid(row=0, column=1,columnspan=2,padx=10, pady=10,sticky=W+E)
 

        # ----- 2nd Row -----
        self.Phone_Label = Label(self.admin_window, text="Phone No.")
        self.Phone_Label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
 
        # Will hold the changing value stored last name
        self.Phone_no_value = StringVar(self.admin_window, value="")
        self.Phone_no_entry = ttk.Entry(self.admin_window,textvariable=self.Phone_no_value)
        self.Phone_no_entry.grid(row=1, column=1,columnspan=2, padx=10, pady=10, sticky=W+E)


             # ----- 3rd Row -----
        self.Adress_Label = Label(self.admin_window, text="Address")
        self.Adress_Label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
 
        # Will hold the changing value stored last name
        self.Address_value = StringVar(self.admin_window, value="")
        self.Address_entry = ttk.Entry(self.admin_window,textvariable=self.Address_value)
        self.Address_entry.grid(row=2, column=1,columnspan=2, padx=10, pady=10, sticky=W+E)
 
        # ----- 4rd Row -----
        self.submit_button = ttk.Button(self.admin_window,text="Submit",command=self.write_record)
        self.submit_button.grid(row=0, column=3,padx=9, sticky=W+E)
 
        self.update_button = ttk.Button(self.admin_window,text="Update",command=self.update_record)
        self.update_button.grid(row=1, column=3,padx=9, sticky=W+E)
 
        self.delete_button = ttk.Button(self.admin_window,text="Delete",command=self.delete_record)
        self.delete_button.grid(row=2, column=3,padx=9, sticky=W+E)
        # ----- 5th Row -----
        self.tree= ttk.Treeview(self.admin_window,selectmode="browse",column=("column1", "column2", "column3","column4"), show='headings')
        self.tree.column("column1",width=100,minwidth=100,stretch=NO)
        self.tree.heading("#1", text="ADMISSION")
        self.tree.column("column2",width=180,minwidth=180,stretch=NO)
        self.tree.heading("#2", text="NAME")
        self.tree.column("column3",width=180,minwidth=180,stretch=NO)
        self.tree.heading("#3", text="PHONE")
        self.tree.column("column4",width=450,minwidth=450,stretch=NO)
        self.tree.heading("#4", text="ADDRESS")
        self.tree.bind("<ButtonRelease-1>",self.selectItem)
        self.tree.bind("<space>",self.selectItem)
        self.tree.tag_configure('1', background='ivory2')
        self.tree.tag_configure('2', background='alice blue')
        self.tree.grid(row=4,column=0,columnspan=4,sticky=W+E,padx=9,pady=9)
 
        Label(self.admin_window,text="Search by Part of NAME or PHONE no").grid(row=5,column=0,columnspan=2,pady=9,padx=9,sticky=E)
        self.search_value = StringVar(self.admin_window, value="")
        Entry(self.admin_window,textvariable=self.search_value).grid(row=5,column=2,pady=9,padx=9,sticky=W+E)
        self.search_button = ttk.Button(self.admin_window,text="Search",command=self.search_record)
        self.search_button.grid(row=5,column=3,pady=9,padx=9,sticky=W+E)
        
        self.refresh_button = ttk.Button(self.admin_window,text="Refresh",command=self.refresh)
        self.refresh_button.grid(row=6, column=2,padx=9,pady=9,sticky=W+E)

        Label(self.admin_window,text="Developed by Python_Coderz_").grid(row=6,column=0,pady=9,padx=9,sticky=W)
        self.reset_button = ttk.Button(self.admin_window,text="Reset Database",command=self.reset_db)
        self.reset_button.grid(row=6, column=3,padx=9,pady=9,sticky=W+E)

        self.setup_db()
        self.admin_window.mainloop()



class signinwindow:
    sqlite_var = 0 #variable to establish connection btw python and sqlite3
    theCursor = 0  #variable to store the indexing cursor   
    curItem=0 #variable to store currently active record

    def setup_db(self):
        try:
            self.sqlite_var = sqlite3.connect('user.db')
            self.theCursor = self.sqlite_var.cursor()
        except:
            print("Could not establish connection to sqlite3")

        try:
            self.theCursor.execute("CREATE TABLE if not exists users(username TEXT NOT NULL UNIQUE,password TEXT NOT NULL);")
        except:
            print("ERROR : Table not created")
        finally:
            self.sqlite_var.commit()

             
    def user_tree_update(self):
        self.tree.delete(*self.tree.get_children())
        self.theCursor.execute("SELECT * FROM users")
        res = self.theCursor.fetchall()
        i=0
        for row in res:
            if(i%2==0):
                self.tree.insert("",END, values=row,tag='1')
            else:
                self.tree.insert("",END, values=row,tag='2')  
            i=i+1                    

    def clear_users(self):

        self.theCursor.execute("DROP TABLE users")
        self.setup_db()
        self.user_tree_update()

    def view_users(self):
        try:
            self.theCursor.execute("SELECT * from users")
            res=self.theCursor.fetchall()
        except:
            print("Couldnt read from users")
        self.x=Tk()
        self.x.title("USERS LIST")
        self.x.resizable(False, False)
        self.x.iconbitmap("logo.ico")

        self.tree= ttk.Treeview(self.x,selectmode="browse",column=("column1", "column2"), show='headings')
        self.tree.heading("#1", text="USERNAME")
        self.tree.heading("#2", text="PASSWORD")
        self.tree.tag_configure('1', background='yellow')
        self.tree.tag_configure('2', background='light green')
        self.tree.grid(row=0,column=0,columnspan=4,sticky=W+E,padx=9,pady=9)
        Button(self.x,text="Clear all users",command=self.clear_users).grid(row=1,column=0,columnspan=4,padx=9,pady=9,sticky=W+E)
        self.user_tree_update()
        self.x.mainloop()



    def new_user(self):
        try:
            if(self.username_text.get()!="" and self.password_text.get()!=""):
                self.theCursor.execute("INSERT INTO users (username,password) VALUES(?,?)",(self.username_text.get(),self.password_text.get()))
                self.signin_window.destroy()
                messagebox.showinfo("NEW USER ADDED","New User Added successfully")
            else:
                messagebox.showwarning("EMPTY INPUT","Username or password missing")

        except sqlite3.IntegrityError:
            messagebox.showerror("DUPLICATE","Username already exists")
        except:
            print("Couln't add user")
        finally:
            self.sqlite_var.commit()
            self.theCursor.execute("SELECT * from users")
            res=self.theCursor.fetchall()
            self.username_text.set("")
            self.password_text.set("")
 

    def __init__(self):
        self.signin_window=Toplevel()
        self.signin_window.title("SIGN-UP")
        self.signin_window.resizable(False, False)
        self.signin_window.iconbitmap("logo.ico")

        self.password_text=StringVar()
        self.username_text=StringVar()

        Label(self.signin_window,text="Sign-Up",font="Ariel").grid(row=0,column=0,sticky=W,pady=10)
        Label(self.signin_window,text="Username : ",font="Ariel, 12").grid(row=1,column=0)
        Label(self.signin_window,text="Password : ",font="Ariel, 12").grid(row=2,column=0,pady=(0,20))
        
        Entry(self.signin_window,font="Ariel, 10",textvariable=self.username_text).grid(row=1,column=1)  
        Entry(self.signin_window,font="Ariel, 10",textvariable=self.password_text).grid(row=2,column=1,pady=(0,20))

        user_add=Button(self.signin_window,font="Ariel, 17",text="Add User",background='white',command=self.new_user)
        user_add.grid(row=1,column=2,rowspan=2,padx=20,pady=(0,20))

        view_existing=Button(self.signin_window,text="View Existing Users",background='white',command=self.view_users)
        view_existing.grid(row=3,column=0,columnspan=4,padx=20,pady=(0,20),sticky=W+E)
        self.setup_db()

        self.signin_window.mainloop()



class loginwindow:
    sqlite_var = 0 #variable to establish connection btw python and sqlite3
    theCursor = 0  #variable to store the indexing cursor   
    curItem=0 #variable to store currently active record

    def setup_db(self):
        try:
            self.sqlite_var = sqlite3.connect('user.db')
            self.theCursor = self.sqlite_var.cursor()
        except:
            print("Could not establish connection to sqlite3")

        try:
            self.theCursor.execute("CREATE TABLE if not exists users(username TEXT NOT NULL,password TEXT NOT NULL);")
        except:
            print("ERROR : Table not created")
        finally:
            self.sqlite_var.commit()


    def logg(self):
        try:
            self.theCursor.execute("SELECT * from users")
            res=self.theCursor.fetchall()
            flag=0
            for x in res:
                if(self.var.get()==1 and self.username_text.get()==x[0] and self.password_text.get()==x[1]):
                    self.login_window.destroy()
                    userwindow()
                    flag=1
            if(self.var.get()==2 and self.username_text.get()=="python" and self.password_text.get()=="coderz"):
                self.login_window.destroy()
                adminwindow()
                flag=1          
            if(flag==0):
                messagebox.showinfo("INVALID","INVALID USERNAME OR PASSWORD")
        except:
            print("ERROR while logging in")
            raise
        finally:
            self.password_text.set("") 
            self.username_text.set("")   

            
    def __init__(self):
       
        self.login_window=Toplevel()
        self.login_window.title("LOGIN")
        self.login_window.resizable(False, False)
        self.login_window.iconbitmap("logo.ico")

        self.password_text=StringVar(self.login_window)
        self.username_text=StringVar(self.login_window)
        self.var=IntVar(self.login_window)

        Label(self.login_window,text="LOGIN",font="Ariel").grid(row=0,column=0,sticky=W,pady=10)
        Label(self.login_window,text="Username : ",font="Ariel, 12").grid(row=1,column=0)
        Label(self.login_window,text="Password : ",font="Ariel, 12").grid(row=2,column=0)
        self.username=Entry(self.login_window,font="Ariel, 10",textvariable=self.username_text).grid(row=1,column=1)
        self.password=Entry(self.login_window,font="Ariel, 10",textvariable=self.password_text,show='*').grid(row=2,column=1)

        self.but=Button(self.login_window,font="Ariel, 17",text="GO",command=self.logg)       
        self.but.grid(row=1,column=2,rowspan=2,padx=20)
  
        self.var.set(1)
  
        Radiobutton(self.login_window,text="User",variable=self.var,value=1).grid(row=3,column=0,pady=15)
        Radiobutton(self.login_window,text="Admin",variable=self.var,value=2).grid(row=3,column=1)

        Label(self.login_window,text="DEFAULT ADMIN\t{ Username : 'python' and Password : 'coderz' }",font="Ariel, 7").grid(row=4,column=0,columnspan=3,sticky=W,pady=(5,0),padx=(3,9))
        Label(self.login_window,text="To login as user Sign-Up from file menu of main window",font="Ariel, 7").grid(row=5,column=0,columnspan=3,sticky=W,pady=(0,5),padx=(3,9))
        Label(self.login_window,text="Follow Python_Coderz_ On Instagram For More Amazing Projects",font="Ariel, 7").grid(row=6,column=0,columnspan=3,sticky=W,pady=(0,5),padx=(3,9))

        self.setup_db()

        self.login_window.mainloop()


class mainwindow():
    
    def create_login(self):   
        try:
            loginwindow() 
        except:
            raise Exception("COULD NOT OPEN LOGIN_WINDOW")
    def create_signin(self):   
        try:
            signinwindow() 
        except:
            raise Exception("COULD NOT OPEN SIGNUP_WINDOW")


    def helpp(self):
        import os,webbrowser
        from urllib.request import pathname2url 
        url = 'file:{}'.format(pathname2url(os.path.abspath('help.html')))
        webbrowser.open(url)


    def quit_window(self): 
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    def __init__(self):    
        self.root=Tk()
        self.root.resizable(False, False)
        self.root.configure(bg='#81ecec')
        self.root.protocol("WM_DELETE_WINDOW",self.quit_window)
        self.root.iconbitmap("logo.ico")
        self.root.title("Student Registration App - @Python_coderz_")         
        self.img = ImageTk.PhotoImage(Image.open("logo.png"))
        self.panel = Label(self.root, image = self.img, bg="#81ecec")
        self.panel.grid(row=0,column=0)

        Label(self.root,text="Register",font="Times, 20",foreground='blue',bg="#81ecec").grid(row=1,column=0,sticky=W+E,padx=40)
        Label(self.root,text="STUDENT REGISTRATION APP",font="Times, 29",foreground='red4',bg="#81ecec").grid(row=2,column=0,sticky=W+E,padx=40)
        Label(self.root,text="This app offers an easy way to manage student records",
        font="Ariel, 12",bg="#81ecec").grid(row=3,column=0,columnspan=2,sticky=W+E,pady=30)
        Label(self.root,text="PLEASE LOGIN TO CONTINUE",
        font="Ariel, 18",bg="#81ecec").grid(row=4,column=0,columnspan=2,sticky=W+E,pady=5)
        self.but=Button(self.root,text="LOGIN",command=self.create_login)
        self.but.configure(width=18,height=2,foreground="white",background="orange4")
        self.but.grid(row=5,column=0,columnspan=2,sticky='N',pady=30)
        
        self.menu_bar=Menu(self.root)

        self.menu_bar.add_separator()

        self.file_menu=Menu(self.menu_bar,tearoff=0)
        self.file_menu.add_command(label="Sign-up",command=self.create_signin)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quit",command=self.quit_window)
        self.menu_bar.add_cascade(label="File",menu=self.file_menu)

        self.menu_bar.add_separator()

        self.help_menu=Menu(self.menu_bar,tearoff=0)
        self.help_menu.add_command(label="Help",command=self.helpp)
        self.menu_bar.add_cascade(label="Help",menu=self.help_menu)
                
        self.root.config(menu=self.menu_bar)
        self.root.mainloop()

try:
    mainwindow()
except:
    raise Exception("COULD  NOT CREATE MAIN_WINDOW")
