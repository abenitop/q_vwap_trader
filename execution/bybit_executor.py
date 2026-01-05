from pybit.unified_trading import HTTP
from dotenv import load_dotenv
import os

load_dotenv()

class BybitExecutor:
    def __init__(self, testnet=False):
        self.session = HTTP(testnet=testnet, api_key=os.getenv("BYBIT_API_KEY"), api_secret=os.getenv("BYBIT_API_SECRET"))
    
    def place_order(self, symbol, side, qty, tp, sl):
        return self.session.place_order(
            category="linear", symbol=symbol, side=side, orderType="Market",
            qty=str(qty), takeProfit=str(round(tp, 2)), stopLoss=str(round(sl, 2)),
            tpTriggerBy="LastPrice", slTriggerBy="LastPrice"
        )
