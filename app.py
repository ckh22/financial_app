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

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Login"
        self.hi_there["command"] = self.login
        self.hi_there.grid(row=0)
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=1)
        self.registerButton = tk.Button(self)
        self.registerButton['text'] = "Register"
        self.registerButton['command'] = self.register
        self.registerButton.grid(row=2)

    def login(self):
        your_username = input("Enter email: ")
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

    def register(self):
        your_username = input("Enter username: ")
        your_password = input("Enter password: ")
        rows = db.register(your_username, your_password)

    
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