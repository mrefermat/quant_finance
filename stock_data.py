import pandas as pd
from alpha_vantage.timeseries import TimeSeries
key ='B22889019-EABCFEE1'

ts = TimeSeries(key=  key, output_format='pandas')

# Function to get adjusted price from alpha vantage
def get_stock_adj_price(ticker):
	data, meta_data = ts.get_daily_adjusted(ticker,outputsize='full')
	data.index = pd.to_datetime(data.index)
	return data['5. adjusted close']