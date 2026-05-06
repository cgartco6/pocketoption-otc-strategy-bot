# Pocket Option OTC Strategy Bot (Katie Tutorials Exact Recreation)

**Indicators**:
- SMA 100 (White)
- ZigZag (Dev 6, Depth 9, Backstep 3, Blue)
- SuperTrend (ATR 9, Mult 2)
- RSI 9 (Pink line, Green/Red bands, White midline)

**Timeframe**: 1m candles | **Expiry**: 3 minutes (or 2)

**Pre-Signal Feature**: Generates "BUY/SELL ALERT" (pre-signal) when conditions are building, then "CONFIRMED SIGNAL" only on full confluence to reduce false entries and prevent losses.

**Features**:
- Real-time signals via Telegram
- Pre-signal + Confirmed signal logic
- Backtesting module
- Configurable

**Warning**: Test in demo. OTC markets can be volatile.
