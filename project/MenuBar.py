
from tkinter import *
from login import Login_Page
class Menu_Bar:
    def menu(self):
        global window
        window=Tk()
        login_obj=Login_Page()
        window.geometry("500x500")
        window.title("Hcl Emp System")
        menubar=Menu(window)
        menubar.add_command(label="login",command=login_obj.loginForm)
        #menubar.add_command(label="newuser",)
        window.config(menu=menubar)
        window.mainloop()