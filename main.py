import asyncio
import pandas as pd
import ccxt
import time
from config import *
from strategy import analyze
from telegram_bot import send_signal

exchange = ccxt.pocketoption({
    'enableRateLimit': True,
    # Add credentials if needed
})

async def main_loop():
    print("Bot started - Monitoring OTC pairs...")
    while True:
        for symbol in SYMBOLS:
            try:
                ohlcv = exchange.fetch_ohlcv(symbol, TIMEFRAME, limit=200)
                df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
                
                direction, sig_type, reason = analyze(df)
                
                if direction:
                    price = df['close'].iloc[-1]
                    await send_signal(sig_type, direction, symbol, price, reason, EXPIRY_MIN)
                    print(f"[{time.strftime('%H:%M:%S')}] {sig_type} {direction} {symbol}")
            except Exception as e:
                print(f"Error {symbol}: {e}")
        await asyncio.sleep(15)  # Check every 15s

if __name__ == "__main__":
    asyncio.run(main_loop())
