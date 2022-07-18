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
Stock='ADP'
steps=10
df_ADP = df1[['NASDAQ.ADP']]
model_adp = ARIMA(df_ADP, order=(1,1,1))

model_adp= model_adp.fit()


pickle.dump(model_adp, open('model_adp.pkl','wb'))

model_adp= pickle.load(open('model_adp.pkl','rb'))
forecast_ADP = model_adp.forecast(steps)
print(forecast_ADP) 