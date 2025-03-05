import time
import threading
import signal
from watcher import ticker
import settings

settings.init()

def signal_handler(sig, frame):
    print("\n🛑 Stop signal received. Ending...")
    settings.stop_event.set()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    hilo_principal = threading.Thread(target=ticker.monitor_stock, args=("NVDA",), daemon=True)
    hilo_principal.start()

    while not settings.stop_event.is_set():
        time.sleep(1)

    print("✅ Programme successfully completed.")