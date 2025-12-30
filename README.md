# OHLCGrabber
Fetch and store historical OHLCV data from Binance for backtesting and quant analysis.

OHLCGrabber is a lightweight tool that fetches historical OHLCV data for any trading pair and interval from Binance, and saves it directly into a CSV file. The CSV is ready to be read by your backtesting or quant scripts. Automatic batching allows fetching large date ranges efficiently without memory issues.

Features

Supports all Binance intervals: 1m, 5m, 1h, 1d, etc.

Saves OHLCV (Open, High, Low, Close, Volume) directly to CSV

Handles large date ranges automatically

Chronological order of candles, ready for backtesting

Minimal terminal interface with progress display

Use Case

Quickly fetch data for backtesting strategies. For example, fetch EURUSD 1-hour candles from January to May in a few seconds. Your backtesting script can then read the CSV and run your strategy without extra setup.

Usage
python ohlcgrabber.py


Example Input:

Pair (e.g., BTCUSDT): EURUSDT
Interval (1m, 5m, 1h, 1d...): 1h
Start (YYYY-MM-DD): 2023-01-01
End (YYYY-MM-DD): 2023-05-01


CSV file is created automatically with all candles in chronological order.
