import matplotlib.pyplot as plt

class Plotter():
    def __init__(self, data):
        self.data = data
    
    def pieChart(self):
        data = self.data
        tickers = []
        percentages = []
        for item in data:
            tickers.append(item.ticker['payload'])
            percentages.append(item.percentage['payload'])
        tickers = tuple(tickers)
        fig1, ax1 = plt.subplots()
        ax1.pie(percentages, labels=tickers, autopct='%1.1f%%',
        shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

        
    def __str__(self):
        return str(self.data)