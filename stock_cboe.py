import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.api import Holt
import re



df = pd.read_csv('stocks.csv',parse_dates=['DATE'],index_col='DATE')
df=df.resample('D').mean()
df1=df
df1=df[['NASDAQ.AAPL','NASDAQ.ADP','NASDAQ.CBOE','NASDAQ.CSCO','NASDAQ.EBAY']]
Stock='CBOE'
steps=10
df_CBOE = df1[['NASDAQ.CBOE']]
model_cboe= ExponentialSmoothing(df_CBOE,trend='multiplicative',seasonal='additive',initialization_method='estimated')
model_cboe = model_cboe.fit(optimized=True)


pickle.dump(model_cboe, open('model_cboe.pkl','wb'))

model_cboe= pickle.load(open('model_cboe.pkl','rb'))
forecast_CBOE = model_cboe.forecast(steps)
print(forecast_CBOE) 