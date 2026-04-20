import respx
import httpx
from httpx import Response

BASE_URL = "https://api.binance.com"


@respx.mock
def test_ticker_24hr(ticker_24h):

    respx.get(f"{BASE_URL}/api/v3/ticker/24hr").mock(
        return_value=Response(200, json=ticker_24h)
    )

    r = httpx.get(f"{BASE_URL}/api/v3/ticker/24hr?symbol=BTCUSDT")

    assert r.status_code == 200
    assert r.json()["symbol"] == "BTCUSDT"


@respx.mock
def test_order_book(depth):

    respx.get(f"{BASE_URL}/api/v3/depth").mock(
        return_value=Response(200, json=depth)
    )

    r = httpx.get(f"{BASE_URL}/api/v3/depth?symbol=BTCUSDT")

    assert "bids" in r.json()
    assert "asks" in r.json()


@respx.mock
def test_exchange_info(exchange_info):

    respx.get(f"{BASE_URL}/api/v3/exchangeInfo").mock(
        return_value=Response(200, json=exchange_info)
    )

    r = httpx.get(f"{BASE_URL}/api/v3/exchangeInfo")

    assert r.json()["symbols"][0]["symbol"] == "BTCUSDT"


@respx.mock
def test_klines():

    respx.get(f"{BASE_URL}/api/v3/klines").mock(
        return_value=Response(
            200,
            json=[[123, "64000", "66000", "63000", "65000", "100"]],
        )
    )

    r = httpx.get(f"{BASE_URL}/api/v3/klines?symbol=BTCUSDT&interval=1h")

    assert isinstance(r.json(), list)


@respx.mock
def test_trades(trades):

    respx.get(f"{BASE_URL}/api/v3/trades").mock(
        return_value=Response(200, json=trades)
    )

    r = httpx.get(f"{BASE_URL}/api/v3/trades?symbol=BTCUSDT")

    assert r.json()[0]["price"] == "65000"