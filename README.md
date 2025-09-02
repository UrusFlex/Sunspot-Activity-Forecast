# Sunspot Activity Forecast

This code implements a time series analysis and forecasting project for sunspot activity data. 

It begins by loading the sunspots dataset from the statsmodels library. The initial step involves checking the stationarity of the time series using the Augmented Dickey-Fuller (ADF) test, which outputs the ADF statistic, p-value, and critical values to determine if the data is non-stationary.

The code then employs an automated process to achieve stationarity by repeatedly differencing the series until the ADF test indicates stationarity (p-value ≤ 0.05). The number of differences required (d) is recorded. An ARIMA model with order (2, d, 2) is fitted to the original sunspot activity data, using the previously determined value of d for the integrated component. Finally, the model generates a 50-step forecast into the future. The results are visualized using matplotlib, plotting both the original historical sunspot activity and the forecasted values on a single graph with appropriate labels and a legend for clarity. 
