from numba import njit
import numpy as np

@njit
def backtest_core(closes, highs, lows, opens, vols, turnovers, dates, atrs, sd_mult, tp_atr, sl_atr):
    n = len(closes)
    vwap = np.zeros(n)
    cum_vol = cum_pv = 0.0
    current_date = dates[0]
    for i in range(n):
        if dates[i] != current_date:
            cum_vol = cum_pv = 0.0
            current_date = dates[i]
        cum_vol += vols[i]
        cum_pv += turnovers[i]
        vwap[i] = cum_pv / cum_vol if cum_vol > 0 else closes[i]
    stds = np.zeros(n)
    lookback = 20
    for i in range(lookback, n):
        stds[i] = np.std(closes[i-lookback:i])
    upper = vwap + sd_mult * stds
    lower = vwap - sd_mult * stds
    trades, returns = 0, []
    in_pos, side, entry_p, entry_atr = False, 0, 0.0, 0.0
    for i in range(lookback, n - 1):
        if in_pos:
            tp_p = entry_p + (entry_atr * tp_atr if side == 1 else -entry_atr * tp_atr)
            sl_p = entry_p - (entry_atr * sl_atr if side == 1 else -entry_atr * sl_atr)
            n_high, n_low = highs[i+1], lows[i+1]
            if (side == 1 and n_low <= sl_p) or (side == -1 and n_high >= sl_p):
                returns.append(-1.0)
                trades += 1
                in_pos = False
            elif (side == 1 and n_high >= tp_p) or (side == -1 and n_low <= tp_p):
                returns.append(tp_atr / sl_atr)
                trades += 1
                in_pos = False
        else:
            c, l, h = closes[i], lows[i], highs[i]
            if l <= lower[i] and c > lower[i]:
                in_pos, side, entry_p, entry_atr = True, 1, opens[i+1], atrs[i]
            elif h >= upper[i] and c < upper[i]:
                in_pos, side, entry_p, entry_atr = True, -1, opens[i+1], atrs[i]
    return np.array(returns), trades
