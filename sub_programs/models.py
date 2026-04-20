from pydantic import BaseModel
from typing import List, Optional


class Price(BaseModel):
    symbol: str
    price: float   # auto converts from string


class Filter(BaseModel):
    filterType: str
    tickSize: Optional[str] = None
    minQty: Optional[str] = None
    stepSize: Optional[str] = None


class Symbol(BaseModel):
    symbol: str
    status: str
    baseAsset: str
    quoteAsset: str
    filters: list[Filter]

    def price_filter(self):
        return next(
            (f for f in self.filters if f.filterType == "PRICE_FILTER"),
            None
        )

    def lot_size(self):
        return next(
            (f for f in self.filters if f.filterType == "LOT_SIZE"),
            None
        )

    def tick_size(self):
        f = self.price_filter()
        return float(f.tickSize) if f else None

    def min_qty(self):
        f = self.lot_size()
        return float(f.minQty) if f else None

    def step_size(self):
        f = self.lot_size()
        return float(f.stepSize) if f else None


class ExchangeInfo(BaseModel):
    symbols: List[Symbol]

class Ticker24hr(BaseModel):
    symbol: str
    priceChange: str
    priceChangePercent: str
    weightedAvgPrice: str
    prevClosePrice: str
    lastPrice: str
    volume: str
    quoteVolume: str
    highPrice: str
    lowPrice: str

class OrderBook(BaseModel):
    lastUpdateId: int
    bids: list[list[str]]
    asks: list[list[str]]

class Trade(BaseModel):
    id: int
    price: str
    qty: str
    time: int
    isBuyerMaker: bool

class Kline(BaseModel):
    open_time: int
    open: str
    high: str
    low: str
    close: str
    volume: str
    close_time: int
    quote_volume: str
    trades: int
    taker_buy_base: str
    taker_buy_quote: str