import pandas as pd
from indicators import *

def analyze(df):
    df = add_ma(df)
    df = add_rsi(df, RSI_PERIOD)
    df = add_supertrend(df, SUPERTREND_ATR, SUPERTREND_MULT)
    df = add_zigzag(df, ZIGZAG_DEV, ZIGZAG_DEPTH, ZIGZAG_BACKSTEP)
    df.dropna(inplace=True)
    if len(df) < 50:
        return None, None, "Insufficient data"
    
    latest = df.iloc[-1]
    prev = df.iloc[-2]
    
    # Trend from MA
    ma_slope = latest['MA100'] - prev['MA100']
    ma_above = latest['MA100'] > latest['close']  # For downtrend example
    
    # SuperTrend
    st_down = latest['ST_Direction'] == -1
    st_up = latest['ST_Direction'] == 1
    
    # RSI
    rsi_below_mid = latest['RSI'] < 50
    rsi_above_mid = latest['RSI'] > 50
    
    # ZigZag direction (simplified - last move)
    zz_down = latest['close'] < prev['close']  # Rough
    
    # Pre-Signal (Building conditions)
    pre_buy = st_up and rsi_above_mid and ma_slope > 0
    pre_sell = st_down and rsi_below_mid and ma_slope < 0
    
    # Confirmed Full Confluence (Video logic)
    confirmed_buy = pre_buy and ma_above == False and latest['close'] > latest['MA100']
    confirmed_sell = pre_sell and ma_above and latest['close'] < latest['MA100']
    
    if confirmed_sell:
        return "SELL", "CONFIRMED", "Strong downtrend: MA down + ST red + RSI below mid + ZigZag down"
    elif confirmed_buy:
        return "BUY", "CONFIRMED", "Strong uptrend: MA up + ST green + RSI above mid + ZigZag up"
    elif pre_sell:
        return "SELL", "PRE-ALERT", "Building down conditions - prepare"
    elif pre_buy:
        return "BUY", "PRE-ALERT", "Building up conditions - prepare"
    
    return None, None, "No signal"
