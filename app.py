import tkinter as tk
import robin_stocks as rs
from auth import Auth
from Position import Position
from azure import Azure

# SQL Azure Server credentials
server = 'mysqlserver-962705397.database.windows.net' 
database = 'mySampleDatabase' 
username = 'azureuser' 
password = 'Azure1234567!' 

# Robinhood auth credentials
your_username = 'clifford.kei.hartley@gmail.com'
your_password = 'wwaaxxdd55297'

auth_data = rs.login(username=your_username,
         password=your_password,
         expiresIn=86400,
         by_sms=True)

db = Azure(server, database, username, password)

user_credentials = Auth(auth_data)
holdings = rs.account.build_holdings()
positionList = []
for key, value in holdings.items():
    position = Position(key, value)
    positionList.append(position)
    print(position)

db.createTable(positionList, 'Positions')



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