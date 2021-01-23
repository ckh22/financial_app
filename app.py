# GUI Interface library
import tkinter as tk

# Robinhood API Library
import robin_stocks as rs

# Auth creds
from Auth import Auth
# Stock Position
from Position import Position
# Azure Database
from Azure import Azure
# Plotting Deps
from Plotter import Plotter

# SQL Azure Server credentials
server = 'mysqlserver-962705397.database.windows.net' 
database = 'mySampleDatabase' 
username = 'azureuser' 
password = 'Azure1234567!' 


# Retrieving robinhood user account holdings
# Will need to implement a checking component here


# Creating an Azure class instance
db = Azure(server, database, username, password)

# Creating & Deleting the initial positions table
# Need to create an update component
# db.deleteTable('Positions')
# db.createInitialTables(positionList, 'Positions')



# from tkinter import *
# import os
 
# # Designing window for registration
 
# def register():
#     global register_screen
#     register_screen = Toplevel(main_screen)
#     register_screen.title("Register")
#     register_screen.geometry("300x250")
 
#     global username
#     global password
#     global username_entry
#     global password_entry
#     username = StringVar()
#     password = StringVar()
 
#     Label(register_screen, text="Please enter details below", bg="blue").pack()
#     Label(register_screen, text="").pack()
#     username_lable = Label(register_screen, text="Username * ")
#     username_lable.pack()
#     username_entry = Entry(register_screen, textvariable=username)
#     username_entry.pack()
#     password_lable = Label(register_screen, text="Password * ")
#     password_lable.pack()
#     password_entry = Entry(register_screen, textvariable=password, show='*')
#     password_entry.pack()
#     Label(register_screen, text="").pack()
#     Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# # Designing window for login 
 
# def login():
#     global login_screen
#     login_screen = Toplevel(main_screen)
#     login_screen.title("Login")
#     login_screen.geometry("300x250")
#     Label(login_screen, text="Please enter details below to login").pack()
#     Label(login_screen, text="").pack()
 
#     global username_verify
#     global password_verify
 
#     username_verify = StringVar()
#     password_verify = StringVar()
 
#     global username_login_entry
#     global password_login_entry
 
#     Label(login_screen, text="Username * ").pack()
#     username_login_entry = Entry(login_screen, textvariable=username_verify)
#     username_login_entry.pack()
#     Label(login_screen, text="").pack()
#     Label(login_screen, text="Password * ").pack()
#     password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
#     password_login_entry.pack()
#     Label(login_screen, text="").pack()
#     Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# # Implementing event on register button
 
# def register_user():
 
#     username_info = username.get()
#     password_info = password.get()
 
#     file = open(username_info, "w")
#     file.write(username_info + "\n")
#     file.write(password_info)
#     file.close()
 
#     username_entry.delete(0, END)
#     password_entry.delete(0, END)
 
#     Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# # Implementing event on login button 
 
# def login_verify():
#     username1 = username_verify.get()
#     password1 = password_verify.get()
#     username_login_entry.delete(0, END)
#     password_login_entry.delete(0, END)
 
#     list_of_files = os.listdir()
#     if username1 in list_of_files:
#         file1 = open(username1, "r")
#         verify = file1.read().splitlines()
#         if password1 in verify:
#             login_sucess()
 
#         else:
#             password_not_recognised()
 
#     else:
#         user_not_found()
 
# # Designing popup for login success
 
# def login_sucess():
#     global login_success_screen
#     login_success_screen = Toplevel(login_screen)
#     login_success_screen.title("Success")
#     login_success_screen.geometry("150x100")
#     Label(login_success_screen, text="Login Success").pack()
#     Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# # Designing popup for login invalid password
 
# def password_not_recognised():
#     global password_not_recog_screen
#     password_not_recog_screen = Toplevel(login_screen)
#     password_not_recog_screen.title("Success")
#     password_not_recog_screen.geometry("150x100")
#     Label(password_not_recog_screen, text="Invalid Password ").pack()
#     Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# # Designing popup for user not found
 
# def user_not_found():
#     global user_not_found_screen
#     user_not_found_screen = Toplevel(login_screen)
#     user_not_found_screen.title("Success")
#     user_not_found_screen.geometry("150x100")
#     Label(user_not_found_screen, text="User Not Found").pack()
#     Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# # Deleting popups
 
# def delete_login_success():
#     login_success_screen.destroy()
 
 
# def delete_password_not_recognised():
#     password_not_recog_screen.destroy()
 
 
# def delete_user_not_found_screen():
#     user_not_found_screen.destroy()
 
 
# # Designing Main(first) window
 
# def main_account_screen():
#     global main_screen
#     main_screen = Tk()
#     main_screen.geometry("300x250")
#     main_screen.title("Account Login")
#     Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
#     Label(text="").pack()
#     Button(text="Login", height="2", width="30", command = login).pack()
#     Label(text="").pack()
#     Button(text="Register", height="2", width="30", command=register).pack()
 
#     main_screen.mainloop()
 
 
# main_account_screen()

# def login(self):
#     your_username = input("Enter Robinhood email: ")
#     your_password = input("Enter your password: ")
#     auth_data = rs.login(username=your_username,
#         password=your_password,
#         expiresIn=86400,
#         by_sms=True)
#     user_credentials = Auth(auth_data)
#     rows = db.login(your_username, bytes(your_password, 'utf-8'))
#     print(rows)
#     for item in self.getPositions():
#         print(item)

# def getPositions(self):
#     holdings = rs.account.build_holdings()
#     positionList = []
#     for key, value in holdings.items():
#         position = Position(key, value)
#         positionList.append(position)
#     return positionList

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.login
        self.hi_there.pack(side="top")
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def login(self):
        your_username = input("Enter Robinhood email: ")
        your_password = input("Enter your password: ")
        
        auth_data = rs.login(username=your_username,
            password=your_password,
            expiresIn=86400,
            by_sms=True)
        user_credentials = Auth(auth_data)
        rows = db.login(your_username, bytes(your_password, 'utf-8'))
        print(rows)
        positionList = self.getPositions()
        plot = Plotter(positionList)
        plot.pieChart()

    
    def getPositions(self):
        holdings = rs.account.build_holdings()
        positionList = []
        for key, value in holdings.items():
            position = Position(key, value)
            positionList.append(position)
        return positionList
        

root = tk.Tk()
app = Application(master=root)
app.mainloop()
rs.logout()