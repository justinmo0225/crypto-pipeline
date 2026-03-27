# Crypto Pipeline — Real-time Bitcoin Tracker

A small real-time data pipeline that fetches Bitcoin prices, persists them to CSV, computes simple technical indicators, generates buy/sell signals, and displays a live plot.

## Quick overview
- Fetch price from CoinGecko using [`getBIT`](api.py) ([api.py](api.py)).
- Append prices to [bitcoin_prices.csv](bitcoin_prices.csv) via [`save`](storage.py) ([storage.py](storage.py)).
- Load and analyze data with [`load_data`](analysis.py), [`add_indicators`](analysis.py), and [`generate_signals`](analysis.py) ([analysis.py](analysis.py)).
- Live visualization and orchestration in [main.py](main.py).

## Files
- [main.py](main.py) — main loop: fetch → save → analyze → plot
- [api.py](api.py) — API client: [`getBIT`](api.py)
- [storage.py](storage.py) — CSV persistence: [`save`](storage.py)
- [analysis.py](analysis.py) — data loading and indicators: [`load_data`](analysis.py), [`add_indicators`](analysis.py), [`generate_signals`](analysis.py)
- [bitcoin_prices.csv](bitcoin_prices.csv) — persisted price history
- [readme.md](readme.md) — this file

## Pipeline details
1. main loop in [main.py](main.py) calls [`getBIT`](api.py) to fetch current BTC/USD.
2. Price is appended to [bitcoin_prices.csv](bitcoin_prices.csv) via [`save`](storage.py).
3. Data is loaded & cleaned with [`load_data`](analysis.py).
4. Indicators added:
   - SMA (10) as `SMA_10`
   - EMA (10) as `EMA_10`
   Implemented in [`add_indicators`](analysis.py).
5. Trading signals (`BUY`, `SELL`, `HOLD`) are derived in [`generate_signals`](analysis.py) by comparing `EMA_10` and `SMA_10`.
6. Last N rows are plotted live with matplotlib in [main.py](main.py).

## Data format
[bitcoin_prices.csv](bitcoin_prices.csv) columns:
- `timestamp` — ISO 8601 timestamp
- `price` — price in USD

## Requirements
- Python 3.10+
- pip packages: requests, pandas, matplotlib

Install:
```sh
pip install requests pandas matplotlib
```

## Run
Start the live pipeline:
```sh
python main.py
```
The program fetches periodically, updates the CSV, and updates the live plot.

## Notes
- API errors are handled simply (prints and skip). See [`getBIT`](api.py).
- SMA uses a 10-point window (initial NaNs expected). EMA gives more weight to recent data. See [`analysis.py`](analysis.py).
- CSV append logic is in [`storage.py`](storage.py).

## License & Contributing
Simple personal project. Contributions and improvements welcome via edits to the repository.