<p align="center">
  <img src="https://avatars.githubusercontent.com/u/75583946?v=4" width="280">
</p>

<p align="center">
  <a href="https://github.com/AymsQuant/OHLCGrabber/stargazers">
    <img src="https://img.shields.io/github/stars/AymsQuant/OHLCGrabber?style=for-the-badge">
  </a>
  <a href="https://github.com/AymsQuant/OHLCGrabber/network/members">
    <img src="https://img.shields.io/github/forks/AymsQuant/OHLCGrabber?style=for-the-badge">
  </a>
  <a href="https://github.com/AymsQuant/OHLCGrabber/issues">
    <img src="https://img.shields.io/github/issues/AymsQuant/OHLCGrabber?style=for-the-badge">
  </a>
  <a href="https://github.com/AymsQuant/OHLCGrabber/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge">
  </a>
</p>

# OHLCGrabber

**OHLCGrabber** is a lightweight Python tool for fetching historical OHLCV (Open, High, Low, Close, Volume) market data from Binance and saving it directly to CSV files. It is designed for simplicity, speed, and reliability, with automatic batching for large date ranges and no API keys required. The output is ready to use in backtesting, quant research, or trading models.

## Features

- Fetch historical OHLCV data for **any Binance pair**  
- Supports all standard intervals: 1m, 5m, 15m, 1h, 1d, etc.  
- Automatically handles large date ranges efficiently  
- Outputs clean CSV files in chronological order  
- Minimal terminal interface with live progress display

## Usage

Run the script and follow the prompts:

```bash
python ohlcgrabber.py
```

Example input:

```
Pair (e.g., BTCUSDT): EURUSDT
Interval (1m, 5m, 1h, 1d): 1h
Start (YYYY-MM-DD): 2023-01-01
End (YYYY-MM-DD): 2023-05-01
```

After fetching, a CSV file is created in the project directory with all candles in the selected range.

## CSV Output

The CSV includes the following columns:

| time                | open   | high   | low    | close  | volume |
|--------------------|--------|--------|--------|--------|--------|
| 2023-01-01 00:00:00 | 1.1234 | 1.1250 | 1.1200 | 1.1220 | 123.45 |

## Why Use OHLCGrabber?

- Eliminates manual API handling  
- Provides ready-to-use CSV for backtesting or ML models  
- Quickly iterate on strategies across pairs, intervals, and date ranges

## Roadmap

- Support for additional exchanges  
- CLI flags for fully non-interactive usage  
- Auto-retry and rate-limit handling  
- Multi-pair batch exports

## License

MIT License — free and open source.

## Contact

AymsQuant — [GitHub Repo](https://github.com/AymsQuant/OHLCGrabber)
