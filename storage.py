import csv
import os
from datetime import datetime

FILE_NAME = "bitcoin_prices.csv"    # creates csv

def save(price):    # saves the price to csv
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline = "") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp", "price"]) # initializes file (timestamp, price)

        writer.writerow([datetime.now().isoformat(), price])