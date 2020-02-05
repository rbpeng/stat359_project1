from alpha_vantage.timeseries import TimeSeries
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

# Example: get_daily_equity_data(outdir="C:/Users/RBP7855/Desktop", filename="test", stock='MSFT', values='all'. num_days=50)