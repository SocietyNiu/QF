import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt;
from datetime import datetime

stockCode='600183'
data = DataAPI.MktEqudAdjAfGet(secID=u"",ticker=stockCode,tradeDate=u"",isOpen="",beginDate=u"",endDate=u"",field=u"secID,secShortName,tradeDate,openPrice,highestPrice,lowestPrice,closePrice,turnoverVol",pandas="1")
data['Daily Return'] = data['closePrice'].pct_change()

sns.distplot(data['Daily Return'].dropna(),color='r')
data.info()
data.describe()
data.plot(x='tradeDate',y='closePrice')
ma_day=[10,20,50]

for ma in ma_day:
    column_name = "MA for %s days" %(str(ma))
    data[column_name] = pd.rolling_mean(data['closePrice'],ma)
data.plot(x='tradeDate',y=['closePrice','MA for 10 days','MA for 20 days','MA for 50 days'],figsize=(12,6))
data.plot(x='tradeDate',y='Daily Return',linestyle='--',marker='o',figsize=(12,6))