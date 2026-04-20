import pytest


@pytest.fixture
def exchange_info():
    return {
        "symbols": [
            {
                "symbol": "BTCUSDT",
                "status": "TRADING",
                "filters": [
                    {"filterType": "PRICE_FILTER", "tickSize": "0.01"},
                    {"filterType": "LOT_SIZE", "minQty": "0.0001", "stepSize": "0.0001"},
                ],
            }
        ]
    }


@pytest.fixture
def ticker_24h():
    return {
        "symbol": "BTCUSDT",
        "lastPrice": "65000.00",
        "priceChangePercent": "2.5",
        "volume": "12345.67",
    }


@pytest.fixture
def depth():
    return {
        "bids": [["65000", "1.2"]],
        "asks": [["65100", "0.8"]],
    }


@pytest.fixture
def trades():
    return [
        {"price": "65000", "qty": "0.01", "time": 123456789}
    ]