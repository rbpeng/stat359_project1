from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange
import numpy as np
import pandas as pd
from pathlib import Path

key = 'M3E8O6PCOLI682KH'

def get_daily_equity_data(outdir, filename, key=key, stock='AAPL', values='all', num_days=100):
    ts = TimeSeries(key, output_format='pandas')
    data, meta = ts.get_daily(symbol=stock, outputsize='full')
    filepath = Path(outdir, filename+'.csv')
    if values=='all':
        data=pd.DataFrame.head(data, n=num_days)
        pd.DataFrame.to_csv(data, filepath, header=True)
        return
    elif values=='open':
        data=pd.DataFrame.head(data[data.columns[0]], n=num_days)
        pd.DataFrame.to_csv(data, filepath, header=True)
        return
    elif values=='high':
        data=pd.DataFrame.head(data[data.columns[1]], n=num_days)
        pd.DataFrame.to_csv(data, filepath, header=True)
        return
    elif values=='low':
        data = pd.DataFrame.head(data[data.columns[2]], n=num_days)
        pd.DataFrame.to_csv(data, filepath, header=True)
        return
    elif values=='close':
        data=pd.DataFrame.head(data[data.columns[3]], n=num_days)
        pd.DataFrame.to_csv(data, filepath, header=True)
        return
    elif values=='volume':
        data=pd.DataFrame.head(data[data.columns[4]], n=num_days)
        pd.DataFrame.to_csv(data, filepath, header=True)
        return
    else:
        print("Error: values must be \'all\', \'open\', \'high\', \'low\', \'close\', or \'volume\'")
        return

# Example: get_daily_equity_data(outdir="C:/Users/RBP7855/Desktop", filename="MSFT", stock='MSFT', values='all', num_days=500)

def get_daily_currency_data(outdir, filename, key=key, curr1='EUR', curr2='USD', values='all', num_days=100):
    fe = ForeignExchange(key, output_format='pandas')
    data, meta = fe.get_currency_exchange_daily(from_symbol=curr1, to_symbol=curr2, outputsize='full')
    filepath = Path(outdir, filename+'.csv')
    if values=='all':
        data=pd.DataFrame.head(data, n=num_days)
        pd.DataFrame.to_csv(data, filepath, header=True)
        return
    options = ['open', 'high', 'low', 'close']
    for i in range(len(options)):
        if values == options[i]:
            data=pd.DataFrame.head(data[data.columns[i]], n=num_days)
            pd.DataFrame.to_csv(data, filepath, header=True)
            return
    else:
        print("Error: values must be \'all\', \'open\', \'high\', \'low\', or \'close\'")
        return

# Example: get_daily_currency_data(outdir="C:/Users/RBP7855/Desktop", filename="JPY_to_USD", curr1='JPY', curr2='USD', values='open', num_days=500)