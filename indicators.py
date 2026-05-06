import pandas as pd
import numpy as np
from utils import atr

def add_ma(df):
    df['MA100'] = df['close'].rolling(window=100).mean()
    return df

def add_rsi(df, period=9):
    delta = df['close'].diff()
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df

def add_supertrend(df, atr_period=9, multiplier=2.0):
    df['ATR'] = atr(df, atr_period)
    hl2 = (df['high'] + df['low']) / 2
    df['UpperBand'] = hl2 + (multiplier * df['ATR'])
    df['LowerBand'] = hl2 - (multiplier * df['ATR'])
    
    df['SuperTrend'] = np.nan
    df['ST_Direction'] = 0  # 1 up, -1 down
    
    for i in range(1, len(df)):
        if df['close'].iloc[i-1] > df['UpperBand'].iloc[i-1]:
            df.loc[df.index[i], 'SuperTrend'] = df['LowerBand'].iloc[i]
            df.loc[df.index[i], 'ST_Direction'] = 1
        elif df['close'].iloc[i-1] < df['LowerBand'].iloc[i-1]:
            df.loc[df.index[i], 'SuperTrend'] = df['UpperBand'].iloc[i]
            df.loc[df.index[i], 'ST_Direction'] = -1
        else:
            df.loc[df.index[i], 'SuperTrend'] = df['SuperTrend'].iloc[i-1]
            df.loc[df.index[i], 'ST_Direction'] = df['ST_Direction'].iloc[i-1]
    return df

def add_zigzag(df, deviation=6, depth=9, backstep=3):
    """Simplified ZigZag - detects significant swings"""
    zz = pd.Series(index=df.index, dtype=float)
    last_pivot = df['close'].iloc[0]
    last_pivot_idx = 0
    direction = 0  # 1 up, -1 down
    
    for i in range(1, len(df)):
        price = df['close'].iloc[i]
        change = abs(price - last_pivot) / last_pivot * 100
        
        if change >= deviation:
            zz.iloc[last_pivot_idx] = last_pivot
            last_pivot = price
            last_pivot_idx = i
            direction = 1 if price > last_pivot else -1
    zz.iloc[last_pivot_idx] = last_pivot
    df['ZigZag'] = zz
    return df
