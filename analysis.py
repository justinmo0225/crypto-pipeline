import pandas as pd

def load_data():    # loads data in correct format & returns for later use
    df = pd.read_csv("bitcoin_prices.csv")  # read csv

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["price"] = pd.to_numeric(df["price"], errors = "coerce")

    df = df.sort_values("timestamp")
    return df

def add_indicators(df):
    # simple moving average (SMA)
    df["SMA_10"] = df["price"].rolling(window = 10).mean()

    # exponential moving average (EMA)
    df["EMA_10"] = df["price"].ewm(span = 10, adjust = False).mean()

    return df

def generate_signals(df):   # creates buy/sell markers based on SMA and EMA
    df["signal"] = "HOLD"

    df.loc[df["EMA_10"] > df["SMA_10"], "signal"] = "BUY"
    df.loc[df["EMA_10"] < df["SMA_10"], "signal"] = "SELL"

    return df

# note that SMA will output NaN between data points 1 to (window - 1) since it is the average of the last 10 data points
# note that, in EMA, .ewm gives more weight to later data points --> allows for a "faster reaction"