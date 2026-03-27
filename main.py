import time
import pandas as pd
import matplotlib.pyplot as plt

from api import getBIT
from storage import save

from analysis import load_data, add_indicators, generate_signals

def main():
    plt.ion()
    fig, ax = plt.subplots()

    while True:
        print("Running pipeline...")

        price = getBIT()

        if price is not None:   # as long as the API does not flag as spam
            print("Bitcoin price:", price)
            save(price)

        # load the data & analyze it
        df = load_data()
        df = add_indicators(df)
        df = generate_signals(df)

        df_plot = df.tail(100)   # displays only the last X points

        # graph!
        ax.clear()

        ax.plot(df_plot["timestamp"], df_plot["price"], label="Price")
        ax.plot(df_plot["timestamp"], df_plot["SMA_10"], label="SMA 10")  # average of the last 10 prices
        ax.plot(df_plot["timestamp"], df_plot["EMA_10"], label="EMA 10")  # average of the last 10 prices, with more weight to the latest prices

        buy = df_plot[df_plot["signal"] == "BUY"]
        sell = df_plot[df_plot["signal"] == "SELL"]

        ax.scatter(buy["timestamp"], buy["price"], color="green", label="BUY", marker="^")  # buy marker
        ax.scatter(sell["timestamp"], sell["price"], color="red", label="SELL", marker="v") # sell marker

        ax.set_title("Live Bitcoin Price")
        ax.set_xlabel("Time")
        ax.set_ylabel("Price (USD $)")
        ax.legend()
        plt.grid(True)

        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.pause(2)   # needed for live intervals

        time.sleep(30)  # API call interval

if __name__ == "__main__":
    main()
    plt.show()