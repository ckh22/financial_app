# Library for Azure Connection
import pyodbc

# Update (1.22.21): Need to add safeguard methods to prevent errors in any of the query methods


class Azure():
    # On init: saves cnxn and cursor
    # Parameters: server, database, username, password
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        self.cursor = self.cnxn.cursor()

    # Fetch query 
    # Parameter: name
    def getTable(self, name):
        query = "SELECT * FROM {name}".format(name=name)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows
        
    # Create table
    # Parameters: list, name
    def createInitialTable(self, list, name):
        createQuery = "CREATE TABLE {name} (\n".format(name=name)
        switch = True
        headerList = {}
        for item in list:
            insertQuery = "INSERT INTO {name}\n".format(name=name) + "VALUES (\n"
            headers = vars(item)
            for key, value in headers.items():
                headerList[key] = value['type']
                insertQuery += "\t" + "'{value}'".format(value=str(value['payload'])) + ",\n"
            insertQuery = insertQuery[:len(insertQuery) - 2]
            insertQuery += "\n)"
            if switch == True:
                self.defineHeaders(headerList, createQuery)
                switch = False
            self.query(insertQuery, 'insert')
    
    # finds the header list headers and creates a query string
    # Parameters: headerList, createQuery
    #   headerList - List containing all of the headers for the Position object
    #   createQuery - query to create a table
    def defineHeaders(self, headerList, createQuery):
        for header in headerList:
                createQuery += "\t" + header + " " + headerList[header] + ",\n"
        createQuery = createQuery[:len(createQuery) - 2]
        createQuery += "\n)"
        self.query(createQuery, 'create')

    # executes the query passed
    # Parameters: query, trigger
    def query(self, query, trigger):
        self.cursor.execute(query)
        self.cnxn.commit()
        if trigger == 'get':
            for row in self.cursor:
                print(row)
        print("Success in executing: {query}".format(query=query))

    # deletes the table with the given name
    # Parameter: name
    def deleteTable(self, name):
        query = "DROP TABLE {name}".format(name=name)
        self.query(query, 'delete')
        