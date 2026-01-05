import pandas as pd
import numpy as np

def calculate_vwap(df: pd.DataFrame, model: str = "anchored", reset_hours: int = 24, rolling_window: int = 90):
    df = df.copy()
    df['dt'] = pd.to_datetime(df['timestamp'], unit='ms')
    if model in ["standard", "anchored"]:
        df['session'] = df['dt'].dt.floor(f'{reset_hours}H')
        df['cum_turnover'] = df.groupby('session')['turnover'].cumsum()
        df['cum_vol'] = df.groupby('session')['volume'].cumsum()
    elif model == "rolling":
        df['cum_turnover'] = df['turnover'].rolling(rolling_window).sum()
        df['cum_vol'] = df['volume'].rolling(rolling_window).sum()
    df['vwap'] = df['cum_turnover'] / df['cum_vol']
    return df
