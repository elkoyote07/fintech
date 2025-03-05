import yfinance as yf
import csv
from datetime import datetime
import settings

def writing_in_csv(ticker, precio):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("nvidia_prices.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, ticker, precio])

def monitor_stock(ticker_symbol, interval=60):
    stock = yf.Ticker(ticker_symbol)
    print(f"📊 Monitoring {ticker_symbol} in real time...")

    while not settings.stop_event.is_set():
        try:
            data = stock.history(period="1d", interval="1m")
            if not data.empty:
                current_price = data['Close'].iloc[-1]
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{timestamp}] {ticker_symbol}: ${current_price:.2f}")

                writing_in_csv(ticker_symbol, current_price)

            settings.stop_event.wait(interval)
        except Exception as e:
            print(f"❌ Error: {e}")

    print("🛑 Stopped monitoring.")