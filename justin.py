import yfinance as yf
import  pandas as pd

# Download Bitcoin data
btc_data = yf.download('BTC-USD', start='2014-09-17', end='2024-11-06', interval='1d')
btc_data.to_csv('bitcoin_data.csv')  # Save to a CSV file

data = pd.read_csv("bitcoin_data.csv")
print(data.columns)