# 🚀 Binance Spot CLI Tool — Development Sprint Plan

##Context

The project aims to create a CLI tool for interacting with the Binance Spot Trading API. It includes tasks for setting up the development environment, implementing market data retrieval, and handling user accounts and orders.

## 🎯 Acceptance Criteria

## Day 1 - API Connectivity: DONE

- Successful API call to testnet. <mark>DONE</mark>

- CLI command binance_cli ping prints server time. <mark>DONE</mark>

## Day 2:

- Wrap and test all read-only market data endpoints.

- CLI command binance_cli info BTCUSDT prints 24h stats and filters.

Day 3:

Static order book displays cleanly with 20 levels each side.

CLI command binance_cli book BTCUSDT prints the snapshot.

Day 4:

Real-time order book updates with binance_cli book BTCUSDT --live.

Day 5:

Live ASCII candlestick chart of BTC/USDT updates in real time.

Day 6:

Authenticated requests work and print testnet balances with binance_cli wallet.

Day 7:

Place and cancel real testnet orders.

Day 8:

Open orders and balances update in real time without polling.

Day 9:

SQLite-backed trade history persists across restarts.

Day 10:

Wallet screen shows real-time P&L for every position.

Day 11:

Shippable v0.1.0 with README, logging, and demo video.

Other information

Deferred to v2 sprint:

Stop-loss, take-profit, OCO orders

Paper trading mode

Rate limiting and circuit breakers

Multiple symbols on a watchlist

Full TUI with textual

CI/CD with pytest, mypy, ruff

Scope-cut rules if behind schedule:

Drop CSV export from Day 9

Drop hide-small-balances toggle from Day 10

Drop demo video from Day 11

Drop Day 10 entirely as last resort

Daily routine suggestion:

30 minutes reading

4 hours coding

30 minutes writing tests

15 minutes commit + push

15 minutes journaling what you learned