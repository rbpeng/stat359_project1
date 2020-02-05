from alpha_vantage.timeseries import TimeSeries
import numpy as np
import pandas as pd
from pathlib import Path

key = 'M3E8O6PCOLI682KH'

def get_daily_equity_data(outdir, filename, key=key, stock='AAPL', values='all'):
    ts = TimeSeries(key, output_format='pandas')
    data, meta = ts.get_daily(symbol=stock)
    filepath = Path(outdir, filename+'.csv')
    if values=='all':
        pd.DataFrame.to_csv(data, filepath, header=True)
        return
    elif values=='open':
        data=data[data.columns[0]]
        pd.DataFrame.to_csv(data, filepath, header=True)
        return
    elif values=='high':
        data=data[data.columns[1]]
        pd.DataFrame.to_csv(data, filepath, header=True)
        return
    elif values=='low':
        data=data[data.columns[2]]
        pd.DataFrame.to_csv(data, filepath, header=True)
        return
    elif values=='close':
        data=data[data.columns[3]]
        pd.DataFrame.to_csv(data, filepath, header=True)
        return
    elif values=='volume':
        data=data[data.columns[4]]
        pd.DataFrame.to_csv(data, filepath, header=True)
        return
    else:
        print("Error: values must be \'all\', \'open\', \'high\', \'low\', \'close\', or \'volume\'")
        return

# Example: get_daily_equity_data(outdir="C:/Users/RBP7855/Desktop", filename="test", stock='MSFT', daily='all')