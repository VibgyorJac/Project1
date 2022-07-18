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
Stock='CSCO'
steps=10
df_CSCO = df1[['NASDAQ.CSCO']]
model_csco = ARIMA(df_CSCO, order=(2,1,1))

model_csco= model_csco.fit()

pickle.dump(model_csco, open('model_csco.pkl','wb'))

model_csco= pickle.load(open('model_csco.pkl','rb'))
forecast_CSCO = model_csco.forecast(steps)
print(forecast_CSCO) 