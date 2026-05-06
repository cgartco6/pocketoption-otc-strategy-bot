import os
from dotenv import load_dotenv
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Strategy Settings (Exact from Video)
MA_PERIOD = 100
ZIGZAG_DEV = 6
ZIGZAG_DEPTH = 9
ZIGZAG_BACKSTEP = 3
SUPERTREND_ATR = 9
SUPERTREND_MULT = 2.0
RSI_PERIOD = 9

TIMEFRAME = '1m'
EXPIRY_MIN = 3

# OTC Pairs (add more as needed)
SYMBOLS = ["EURUSD-OTC", "GBPUSD-OTC", "USDJPY-OTC", "AUDUSD-OTC", "NZDUSD-OTC"]

# Risk
AMOUNT = 1  # % or fixed
