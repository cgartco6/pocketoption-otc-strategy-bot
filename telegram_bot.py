import asyncio
from telegram import Bot
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

async def send_signal(signal_type, direction, symbol, price, reason, expiry):
    bot = Bot(token=TELEGRAM_TOKEN)
    emoji = "🟢" if direction == "BUY" else "🔴"
    msg = f"""
{emoji} **{signal_type} {direction}**
Symbol: {symbol}
Price: {price:.5f}
Reason: {reason}
Expiry: {expiry} minutes
Time: OTC Market
    """
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=msg, parse_mode='Markdown')
