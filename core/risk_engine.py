def calculate_position_size(equity: float, atr: float, sl_atr_mult: float, risk_pct: float, price: float, max_position_pct: float = 0.10):
    risk_amt = equity * risk_pct
    sl_dist = atr * sl_atr_mult
    raw_qty = risk_amt / sl_dist
    max_qty_by_value = (equity * max_position_pct) / price
    qty = min(raw_qty, max_qty_by_value)
    return round(qty, 3)
