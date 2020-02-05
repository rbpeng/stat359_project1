# Project 1: Data Acquisition

## Daily Equity Data

The function `get_daily_equity_data` gets daily equity data from Alpha Vantage. It takes inputs `outdir`, which is simply the path to the desired output directory, `filename`, the name of the output csv file, `key`, your Alpha Vantage API key (if you have one, otherwise leave it blank), `stock`, the name of the equity of your choice (example: 'MSFT'), `values`, which can be 'all', 'open', 'high', 'low', 'close', or 'volume' (for example, if you put 'high', it will give the highest value of the equity each day), and `num_days`, which specifies how many days of data we should get (starting from most recent day, the default is 100).

## Daily Currency Exchange Data

The function `get_daily_currency_data` gets daily currency exchange rate data from Alpha Vantage. It takes inputs `outdir`, which is simply the path to the desired output directory, `filename`, the name of the output csv file, `key`, your Alpha Vantage API key (if you have one, otherwise leave it blank), `curr1`, the name of the starting currency you wish to convert (Ex: 'EUR'), `curr2`, the name of the currency you wish to convert `curr1` into (Ex: 'USD'), `values`, which can be 'all', 'open', 'high', 'low', or 'close' (for example, if you put 'low', it will give the lowest exchange value each day), and `num_days`, which specifies how many days of data we should get (starting from most recent day, the default is 100).

## Currency Exchange Data by Time Interval (Intraday)

The function `get_intraday_currency_data` gets intraday currency exchange rate data from Alpha Vantage at specified intervals (Ex: each 15 minutes). It takes inputs `outdir`, which is simply the path to the desired output directory, `filename`, the name of the output csv file, `key`, your Alpha Vantage API key (if you have one, otherwise leave it blank), `curr1`, the name of the starting currency you wish to convert (Ex: 'EUR'), `curr2`, the name of the currency you wish to convert `curr1` into (Ex: 'USD'), `values`, which can be 'all', 'open', 'high', 'low', or 'close' (for example, if you put 'low', it will give the lowest exchange value each day), `num_obs`, which specifies how many data observations we should get (starting from most recent observation, the default is 100), and `interval`, which specifies the interval of time between each successive observation (possible options are '1min', '5min', '15min', '30min', and '60min'). 
