import pandas as pd
import numpy as np

def generate_signals(df: pd.DataFrame, sd_mult: float):
    df = df.copy()
    lookback = 20
    df['std'] = df['close'].rolling(lookback).std()
    df['upper'] = df['vwap'] + sd_mult * df['std']
    df['lower'] = df['vwap'] - sd_mult * df['std']
    signals = pd.Series(0, index=df.index)
    for i in range(1, len(df)):
        prev, curr = df.iloc[i-1], df.iloc[i]
        if prev['low'] <= prev['lower'] and curr['close'] > curr['lower']:
            signals.iloc[i] = 1
        elif prev['high'] >= prev['upper'] and curr['close'] < curr['upper']:
            signals.iloc[i] = -1
    return signals
