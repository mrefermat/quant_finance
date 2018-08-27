import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.sectorperformance import SectorPerformances
key ='B22889019-EABCFEE1'



# Function to get adjusted price from alpha vantage
def get_stock_adj_price(ticker):
	ts = TimeSeries(key=key, output_format='pandas')
	data, meta_data = ts.get_daily_adjusted(ticker,outputsize='full')
	data.index = pd.to_datetime(data.index)
	return data['5. adjusted close']

def get_sector_data():
	sp=SectorPerformances (key=key, output_format='pandas')
	data,_ = sp.get_sector()
	df = pd.DataFrame()
	df['1M Performane']=data['Rank D: Month Performance']
	df['YTD Performance']=data['Rank F: Year-to-Date (YTD) Performance']
	df['1Y Performance']=data['Rank G: Year Performance']
	df['3Y Performance']=(data['Rank H: Year Performance']+1)**.33333333-1
	df['10Y Performance']=(data['Rank J: Year Performance']+1)**.1-1
	return df
