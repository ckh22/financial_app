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

# SQL Azure Server credentials
server = 'mysqlserver-962705397.database.windows.net' 
database = 'mySampleDatabase' 
username = 'azureuser' 
password = 'Azure1234567!' 

# Robinhood auth credentials

auth_data = rs.login(username=your_username,
         password=your_password,
         expiresIn=86400,
         by_sms=True)
user_credentials = Auth(auth_data)

# Retrieving robinhood user account holdings
# Will need to implement a checking component here
holdings = rs.account.build_holdings()
positionList = []
for key, value in holdings.items():
    position = Position(key, value)
    positionList.append(position)


# Creating an Azure class instance
db = Azure(server, database, username, password)

# Creating & Deleting the initial positions table
# Need to create an update component
# db.deleteTable('Positions')
# db.createInitialTable(positionList, 'Positions')
rows = db.getTable("Positions")
print(rows)

# Creating an software gui through tk
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
rs.logout()