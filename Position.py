class Position():
    def __init__(self, ticker, json):
        self.ticker = ticker
        self.json = json
        self.price = {'type': 'String', 'payload': json['price']}
        self.quantity = {'type': 'String', 'payload': json['quantity']}
        self.average_buy_price = {'type': 'String', 'payload': json['average_buy_price']}
        self.equity = {'type': 'String', 'payload': json['equity']}
        self.percent_change = {'type': 'String', 'payload': json['percent_change']}
        self.equity_change = {'type': 'String', 'payload': json['equity_change']}
        self.type = {'type': 'String', 'payload': json['type']}
        self.name = {'type': 'String', 'payload': json['name']}
        self.id = {'type': 'String', 'payload': json['id']}
        self.pe_ratio = {'type': 'String', 'payload': json['pe_ratio']}
        self.percentage = {'type': 'String', 'payload': json['percentage']}
    def __str__(self):
        return self.ticker