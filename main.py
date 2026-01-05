import os, time, yaml
from dotenv import load_dotenv
from core.vwap_engine import calculate_vwap
from execution.bybit_executor import BybitExecutor
from monitoring.logger import emit_event
from adapters.bybit_data import fetch_ohlcv

with open("config/config.yaml") as f:
    CONFIG = yaml.safe_load(f)

load_dotenv()
SYMBOL = os.getenv("SYMBOL", "BTCUSDT")
TIMEFRAME = os.getenv("TIMEFRAME", "5")

def run_bot():
    emit_event("SYSTEM", "🚀 Q-VWAP Trader Active")
    executor = BybitExecutor()
    while True:
        try:
            df = fetch_ohlcv(executor.session, SYMBOL, TIMEFRAME, 200)
            time.sleep(10)
        except Exception as e:
            emit_event("ERROR", str(e))
        time.sleep(10)

if __name__ == "__main__":
    run_bot()
