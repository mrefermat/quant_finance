import pandas as pd
import numpy as np
import math
import quandl as q
token="Us3wFmXGgAj_1cUtHAAR"

# Simple Sharpe ratio calculation
def calc_Sharpe(pnl,N=12):
    return np.sqrt(N) * pnl.mean() / pnl.std()

# Simple 50/50 risk parity calculation based on S&P 500 / US Treasuries
def calc_risk_parity(vol=.1,lookback=36):
    df=pd.DataFrame()
    df['SP500']=q.get("CHRIS/CME_SP1", authtoken=token).resample(rule='m').last().Last
    df['US10Y']=q.get("CHRIS/CME_US1", authtoken=token).resample(rule='m').last().Last
    data_pct=df.pct_change()
    rtns=((data_pct/pd.DataFrame.ewm(data_pct,lookback,min_periods=lookback/3.).std())*(vol/math.sqrt(12))).dropna()
    mat=pd.DataFrame.ewm(data_pct,lookback,min_periods=lookback/3.).corr().dropna()
    sf=pd.Series()
    for d,dd in mat.groupby(level=0):
        sf[d]=1/math.sqrt(dd.mean().mean())
    return rtns.multiply(sf,axis=0).dropna().mean(axis=1)

# Yield to return 
def yields_to_rtn_index(yld):
    s = pd.Series()
    last=4.06
    for timestamp,yi in yld.iteritems():
        interest = last/12.
        change=np.pv(yi/100.,10,-last,fv=-100)-100
        last=yi
        s[timestamp]=change+interest
    return s/100.

# time series of bond returns
def get_bond_time_series():
	yld=q.get("FRED/DGS10", authtoken=token).Value
	return yields_to_rtn_index(yld.resample(rule='m').last())

def get_sp():
    return q.get('MULTPL/SP500_REAL_PRICE_MONTH' , authtoken=token).Value.resample(rule='m').last()

# Has data only until November 2018.  Come on quandl!!!
def get_libor():
    return q.get("ECB/RTD_M_S0_N_C_USL3M_U", authtoken=token)['Percent per annum']


