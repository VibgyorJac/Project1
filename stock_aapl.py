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
Stock='AAPL'
steps=10
df_AAPL = df1[['NASDAQ.AAPL']]
model_DES = Holt(df_AAPL,exponential=False, initialization_method='estimated')
model_DES = model_DES.fit(optimized=True)


pickle.dump(model_DES, open('model_aapl.pkl','wb'))

model_aapl= pickle.load(open('model_aapl.pkl','rb'))
forecast_AAPL = model_aapl.forecast(steps)
print(forecast_AAPL) 