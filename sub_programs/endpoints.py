import requests
import sub_programs.helpers as helper
from sub_programs.models import ExchangeInfo, Price, Ticker24hr, OrderBook, Trade, Kline

BASE_URL = "https://testnet.binance.vision/api/v3"


# -------------------------
# Main entry
# -------------------------
def get_crypto_information(symbol: str):

    symbol = symbol.upper()

    exchange_info = get_exchange_info(symbol)

    if not exchange_info or not exchange_info.symbols:
        print(f"\n\tSymbol Pair: '{symbol}' does not exist.\n")
        return

    symbol_data = exchange_info.symbols[0]

    price_data = get_price(symbol)

    if not price_data:
        print(f"\n\tCould not fetch price for '{symbol}'\n")
        return

    display_all_crypto_details(symbol_data, price_data)


# -------------------------
# API calls
# -------------------------
def get_exchange_info(symbol):
    url = f"{BASE_URL}/exchangeInfo"

    try:
        r = requests.get(url, params={"symbol": symbol}, timeout=5)
        r.raise_for_status()
        return ExchangeInfo.model_validate(r.json())

    except requests.exceptions.RequestException as e:
        print("\n\tExchange Info Error:", e)
        return None


def get_price(symbol):
    url = f"{BASE_URL}/ticker/price"

    try:
        r = requests.get(url, params={"symbol": symbol}, timeout=5)
        r.raise_for_status()
        return Price.model_validate(r.json())

    except requests.exceptions.RequestException as e:
        print("\n\tPrice Error:", e)
        return None


def get_24hr_ticker(symbol: str):
    url = f"{BASE_URL}/ticker/24hr"

    try:
        r = requests.get(url, params={"symbol": symbol}, timeout=5)
        r.raise_for_status()
        return Ticker24hr.model_validate(r.json())

    except requests.exceptions.RequestException as e:
        print("\n\t24hr Error:", e)
        return None


def get_order_book(symbol: str, limit: int = 100):
    url = f"{BASE_URL}/depth"

    try:
        r = requests.get(url, params={"symbol": symbol, "limit": limit}, timeout=5)
        r.raise_for_status()
        return OrderBook.model_validate(r.json())

    except requests.exceptions.RequestException as e:
        print("\n\tDepth Error:", e)
        return None

#Candles/Klines
def get_klines(symbol: str, interval: str = "1m", limit: int = 100):
    url = f"{BASE_URL}/klines"

    try:
        r = requests.get(
            url,
            params={"symbol": symbol, "interval": interval, "limit": limit},
            timeout=5,
        )
        r.raise_for_status()

        data = r.json()

        return [
            Kline(
                open_time=x[0],
                open=x[1],
                high=x[2],
                low=x[3],
                close=x[4],
                volume=x[5],
                close_time=x[6],
                quote_volume=x[7],
                trades=x[8],
                taker_buy_base=x[9],
                taker_buy_quote=x[10],
            )
            for x in data
        ]

    except requests.exceptions.RequestException as e:
        print("\n\tKlines Error:", e)
        return None

#Command Example - binance_cli trades BTCUSDT 
def get_trades(symbol: str, limit: int = 100):
    url = f"{BASE_URL}/trades"

    try:
        r = requests.get(url, params={"symbol": symbol, "limit": limit}, timeout=5)
        r.raise_for_status()

        return [Trade.model_validate(x) for x in r.json()]

    except requests.exceptions.RequestException as e:
        print("\n\tTrades Error:", e)
        return None


# -------------------------
# Display logic
# -------------------------
def display_all_crypto_details(symbol_data, price_data):

    symbol = symbol_data.symbol
    status = symbol_data.status
    price = price_data.price

    tick_size = symbol_data.tick_size()
    min_qty = symbol_data.min_qty()
    step_size = symbol_data.step_size()

    details = [
        f"Symbol: {symbol}",
        f"Price: ${price}",
        f"Status: {status}",
        f"Tick Size: {tick_size}",
        f"Min Qty: {min_qty}",
        f"Step Size: {step_size}",
    ]

    helper.box_items(details, f"{symbol} Info")