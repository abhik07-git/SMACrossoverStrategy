import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
#Import necessary libraries

ticker = input("Enter the stock symbol you wish to track: (ex. AAPL): ").upper()
#Lets the user type in a stock symbol


end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')
#Gets the current date and sets the start date to the year prior

data = yf.download(ticker, start = start_date, end = end_date, interval = "1h")
#Downloads hourly prices from Yahoo Finance

data['SMA_20'] = data['Close'].rolling(window = 20).mean()
data['SMA_100'] = data['Close'].rolling(window = 100).mean()
#SMA = Simple Moving Average: The program takes the average of the last 20 and last 100 closing prices

data['Signal'] = (data['SMA_20'] > data['SMA_100']).astype(int)

data['Position'] = data['Signal'].diff()
#If 20 day is greater than 100 day, buy indicator, otherwise sell indicator

plt.style.use('seaborn-v0_8-darkgrid')

plt.figure(figsize=(16,8))
plt.plot(data['Close'], label = 'Closing Price', alpha = 0.5)
plt.plot(data['SMA_20'], label = '20-Day SMA', color = 'green', linewidth = 2)
plt.plot(data['SMA_100'], label = '100-Day SMA', color = 'red', linewidth = 2)
#Sets graph style and plots price, SMA 20 day, and SMA 100 day graphs

plt.plot(data.loc[data['Position'] == 1].index,
         data.loc[data['Position'] == 1, 'SMA_20'],
         '^', markersize=12, color='green', label='Buy Signal')

plt.plot(data.loc[data['Position'] == -1].index,
         data.loc[data['Position'] == -1, 'SMA_20'],
         'v', markersize=12, color='red', label='Sell Signal')
#Places green arrows at buy locations and red arrows at sell locations

plt.title(f"{ticker} - SMA Crossover Strategy ({start_date} to {end_date})", fontsize = 16)
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.xticks(rotation = 45)
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()
#Final plot labeling and presentation

