def test_ticker_24h(ticker_24h):
    assert ticker_24h["symbol"] == "BTCUSDT"
    assert "lastPrice" in ticker_24h


def test_depth(depth):
    assert "bids" in depth
    assert "asks" in depth


def test_trades(trades):
    assert len(trades) > 0
    assert "price" in trades[0]