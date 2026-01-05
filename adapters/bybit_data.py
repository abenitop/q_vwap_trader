from pybit.unified_trading import HTTP
import pandas as pd

def fetch_ohlcv(session, symbol, interval, limit=200):
    r = session.get_kline(category="linear", symbol=symbol, interval=interval, limit=limit)
    if r['retCode'] != 0: raise Exception(r['retMsg'])
    df = pd.DataFrame(r['result']['list'], columns=['timestamp','open','high','low','close','volume','turnover'])
    return df.iloc[::-1].reset_index(drop=True).astype(float)
