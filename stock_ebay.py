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
Stock='EBAY'
steps=10
df_EBAY = df1[['NASDAQ.EBAY']]
model_ebay = ARIMA(df_EBAY, order=(1,1,1))

model_ebay= model_ebay.fit()


pickle.dump(model_ebay, open('model_ebay.pkl','wb'))

model_ebay= pickle.load(open('model_ebay.pkl','rb'))
forecast_EBAY = model_ebay.forecast(steps)
print(forecast_EBAY) 