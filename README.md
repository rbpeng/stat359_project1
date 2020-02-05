# Project 1: Data Acquisition

## Daily Equity Data

The function `get_daily_equity_data` gets daily equity data from Alpha Vantage. It takes inputs `outdir`, which is simply the path to the desired output directory, `filename`, the name of the output csv file, `key`, your Alpha Vantage API key (if you have one, otherwise leave it blank), `stock`, the name of the equity of your choice (example: 'MSFT'), `values`, which can be 'all', 'open', 'high', 'low', 'close', or 'volume' (for example, if you put 'high', it will give the highest value of the equity each day), and `num_days`, which specifies how many days of data we should get (starting from most recent day, the default is 100).
