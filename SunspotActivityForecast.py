import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA

sunspots = sm.datasets.sunspots.load_pandas().data
print(sunspots.head())
sunspots['YEAR'] = pd.to_datetime(sunspots['YEAR'], format='%Y')
sunspots.set_index('YEAR', inplace = True)

adf_test = adfuller(sunspots)
adf_statistic = adf_test[0]
p_value = adf_test[1]
critical_values = adf_test[4]
print('ADF Statistic:', adf_statistic)
print('p-value:', p_value)
print('Critical values:')
for key, value in critical_values.items():
    print(f' {key}: {value}')

diff_data = sunspots['SUNACTIVITY']
d = 0
while True:
    result = adfuller(diff_data)
    if result[1] <= 0.05:
        print(f'Stationarity is achieved at d =', d)
        break
    diff_data = diff_data.diff().dropna()
    d += 1

model = ARIMA(sunspots['SUNACTIVITY'], order=(2, d, 2))
model_fit = model.fit()

forecast = model_fit.forecast(steps=50)

plt.figure(figsize=(12, 6))
plt.plot(sunspots['SUNACTIVITY'], label='Original series', color='blue')
plt.plot(pd.date_range(sunspots.index[-1], periods=50, freq='YE'), forecast, label='Forecast', color='orange')
plt.title('Sunspot Activity Forecast')
plt.xlabel('Year')
plt.ylabel('Activity')
plt.legend()
plt.show()