import pyodbc

class Azure():
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        self.cursor = self.cnxn.cursor()
    def createTable(self, list, name):
        query = "CREATE {name}(".format(name=name)
        # For loop to create data from list
        headerList = None
        for item in list:
            if headerList == None:
                # finding headers
                headers = vars(item)
                headerList = headers.keys()

            print(item)
        print(headerList)            

        # self.cursor.execute("CREATE  Test(name integer)")
        # self.cnxn.commit()
        