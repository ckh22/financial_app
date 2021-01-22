# A single instance of a stock

class Position():
    # saves the stock information
    # Parameters: ticker, json 
    def __init__(self, ticker, json):
        self.ticker = {'type': 'varchar(255)', 'payload': ticker}
        self.price = {'type': 'varchar(255)', 'payload': json['price']}
        self.quantity = {'type': 'varchar(255)', 'payload': json['quantity']}
        self.average_buy_price = {'type': 'varchar(255)', 'payload': json['average_buy_price']}
        self.equity = {'type': 'varchar(255)', 'payload': json['equity']}
        self.percent_change = {'type': 'varchar(255)', 'payload': json['percent_change']}
        self.equity_change = {'type': 'varchar(255)', 'payload': json['equity_change']}
        self.type = {'type': 'varchar(255)', 'payload': json['type']}
        self.name = {'type': 'varchar(255)', 'payload': json['name']}
        self.id = {'type': 'varchar(255)', 'payload': json['id']}
        self.pe_ratio = {'type': 'varchar(255)', 'payload': json['pe_ratio']}
        self.percentage = {'type': 'varchar(255)', 'payload': json['percentage']}
    def __str__(self):
        return self.ticker['payload']