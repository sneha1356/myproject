from tkinter import *
from tkinter import messagebox
from Database import Mysql_Connector
import tkinter as tk
from PIL import Image,ImageTk

class Login_Page():
    def __init__(self):
        self.db_obj = Mysql_Connector(host="localhost", user='root', passwd='password', db='hcl')
    def check(self):
        self.user1=username.get()
        self.passw1=password.get()
        self.con_pass=confirm_password.get()
        if self.passw1==self.con_pass:
            self.db_obj.insert_db(self.user1,self.passw1)
            messagebox.showinfo('Message','successfully signin go and login')
        else:
            messagebox.showerror('error','must match password and confirm password')
    def sign_Up(self):
        global window2
        window2 = Toplevel(window)
        window2.geometry('400x250+200+200')
        window2.title('Sign up Sysytem')
        global username
        global password
        global confirm_password
        username = StringVar()
        password = StringVar()
        confirm_password = StringVar()
        Label(window2, width="300", text="Enter details Below", bg='orange', fg="white").pack()
        Label(window2, text="UserName ").place(x=20, y=60)
        Entry(window2, textvariable=username).place(x=100, y=62)
        Label(window2, text="password ").place(x=25, y=100)
        Entry(window2, textvariable=password, show='*').place(x=100, y=102)
        Label(window2, text="conf_passwd *").place(x=10, y=140)
        Entry(window2, textvariable=confirm_password, show='*').place(x=100, y=142)
        button = Button(window2, text='signup', command=self.check).place(x=140, y=180)
        # button1=Button(window1,text='register',command=newUser)
        window2.mainloop()

    def validateLogin(self):
        self.user=username.get()
        self.passw=password.get()
        result=self.db_obj.check_User(self.user)
        if result:
            messagebox.showinfo('Message','Login Success')
        else:
            messagebox.showerror('Error','go and signup')
    def serach_Db(self):
        self.user = Userid.get()
        result = self.db_obj.search(int(self.user))
        d={}
        r1=list(result)
        d['username']=r1[1]
        d['password']=r1[2]
        messagebox.showinfo('Details',d)


    def search_window(self):
        global window3
        window3=Toplevel(window)
        window3.geometry('400x250+200+200')
        window3.title('Hcl Emp Sysytem')
        global Userid
        Userid = StringVar()
        Label(window3, width="300", text="Search employee Details", bg='orange', fg="white").pack()
        Label(window3, text="UserID ").place(x=20, y=60)
        Entry(window3, textvariable=Userid).place(x=100, y=62)
        global search
        search = StringVar()
        l2 = Label(window3, textvariable=search, width="300").place(x=150, y=150)
        search.set("")
        button = Button(window3, text='search', command=self.serach_Db).place(x=140,y=100)

        window3.mainloop()
    def loginForm(self):
        global window1
        window1=Toplevel(window)
        window1.geometry('400x250+200+200')
        #window1['background']='#856ff8'
        window1.title('Hcl Emp Sysytem')
        global username
        global password
        global message
        username=StringVar()
        password=StringVar()
        message=StringVar()
        Label(window1,width="300",text="Enter details Below",bg='orange',fg="white").pack()
        Label(window1,text="UserName").place(x=20,y=60)
        Entry(window1,textvariable=username).place(x=100,y=62)
        Label(window1, text="password").place(x=20, y=100)
        Entry(window1,textvariable=password,show='*').place(x=100,y=102)
        button=Button(window1,text='Login',command=self.validateLogin).place(x=150,y=150)
        #button1=Button(window1,text='register',command=newUser)
        window1.mainloop()
    def menu(self):
        global window
        window=Tk()
        window.geometry("500x500")
        window.title("Hcl Emp System")
        # frame=Frame(window,width=200,height=200)
        # frame.pack()
        # bgimg=tk.PhotoImage(file="/home/siri/Documents/Login project/index1.png")
        # img=bgimg.resize((450,350))
        # limg=Label(window,i=bgimg)
        # limg.pack()
        image=Image.open("/home/siri/Documents/project/index1.png")
        img=image.resize((550,500))
        my_img=ImageTk.PhotoImage(img)
        label=Label(window,image=my_img)
        label.pack()
        menubar=Menu(window,background='blue',fg='white')
        menubar.add_command(label="login",command=self.loginForm)
        menubar.add_command(label="signup", command=self.sign_Up)
        menubar.add_command(label="search", command=self.search_window)
        #menubar.add_command(label="newuser",)
        window.config(menu=menubar)
        window.mainloop()
obj=Login_Page()
obj.menu()
