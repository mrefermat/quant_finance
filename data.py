import quandl
token='QWe8iSbyAFzRuod2aroM'


def get_futures_data():

	mkts={'SP 500':'CHRIS/CME_SP1',
	      'Crude Oil':'CHRIS/CME_CL1',
	      'Dollar Index':'CHRIS/ICE_DX1',
	      'Wheat':'CHRIS/CME_W1',
	      'Euro':'CHRIS/CME_EC1',
	      'GBP':'CHRIS/CME_BP1',
	      'Gold':'CHRIS/CME_EC1'
	      }
	data_index=pd.DataFrame()
	for m in mkts.keys():
		try:
			data_index[m]=quandl.get(mkts[m],authtoken=token).Last
		except:
			try:
				data_index[m]=quandl.get(mkts[m],authtoken=token).Settle
			except:
				try:
					data_index[m]=quandl.get(mkts[m],authtoken=token).Value
				except:
					try:
						data_index[m]=quandl.get(mkts[m],authtoken=token).value
					except:
						try:
							data_index[m]=quandl.get(mkts[m],authtoken=token).Rate
						except:
							print(m)
	data_pct=data_index.pct_change()
	return data_index[['SP 500', 'Crude Oil', 'Dollar Index',  'Wheat',
       'Euro', 'GBP', 'Gold']]['2007':].dropna().pct_change().dropna()

