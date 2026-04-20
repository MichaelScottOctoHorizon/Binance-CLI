import sub_programs.helpers as helpers
import sub_programs.binance_test_net as api
import sub_programs.endpoints as endpoint


# This function is the main entry point for the CLI app
def main_application():

    while True:
        cli_command = input("\n\tEnter a CLI command here: ")

        if cli_command.lower() == "exit":
            break

        run_command(cli_command)


# ----------------------------
# CORE LOGIC (TESTABLE PART)
# ----------------------------
def run_command(command: str):
    parts = command.split()

    if len(parts) == 0:
        return

    if parts[0] != "binance_cli":
        print("Invalid command")
        return

    if len(parts) < 2:
        print("Incomplete command")
        return

    action = parts[1]

    # ------------------------
    # ping
    # ------------------------
    if action == "ping":
        api.get_server_time()

    # ------------------------
    # info BTCUSDT
    # ------------------------
    elif action == "info" and len(parts) == 3:
        symbol = parts[2].upper()
        endpoint.get_crypto_information(symbol)

    # ------------------------
    # price BTCUSDT
    # ------------------------
    elif action == "price" and len(parts) == 3:
        symbol = parts[2].upper()
        helpers.box_items(endpoint.get_price(symbol), f"Price of {symbol}")

    # ------------------------
    # 24hr BTCUSDT
    # ------------------------
    elif action == "24hr" and len(parts) == 3:
        symbol = parts[2].upper()
        helpers.box_items(endpoint.get_24hr_ticker(symbol), f"24hr: {symbol}")

    # ------------------------
    # depth BTCUSDT
    # ------------------------
    elif action == "depth" and len(parts) == 3:
        symbol = parts[2].upper()
        helpers.box_items(endpoint.get_order_book(symbol), f"Depth: {symbol}")

    # ------------------------
    # klines BTCUSDT 1h
    # ------------------------
    elif action == "klines" and len(parts) == 4:
        symbol = parts[2].upper()
        interval = parts[3]
        helpers.box_items(
            endpoint.get_klines(symbol, interval),
            f"Klines: {symbol}"
        )

    # ------------------------
    # trades BTCUSDT
    # ------------------------
    elif action == "trades" and len(parts) == 3:
        symbol = parts[2].upper()
        helpers.box_items(endpoint.get_trades(symbol), f"Trades: {symbol}")

    # ------------------------
    # filters BTCUSDT
    # ------------------------
    elif action == "filters" and len(parts) == 3:
        symbol = parts[2].upper()

        exchange = endpoint.get_exchange_info(symbol)

        if not exchange or not exchange.symbols:
            print("Invalid symbol")
            return

        s = exchange.symbols[0]

        lines = [
            f"Symbol: {s.symbol}",
            f"Tick Size: {s.tick_size()}",
            f"Min Qty: {s.min_qty()}",
            f"Step Size: {s.step_size()}",
        ]

        helpers.box_items(lines, "Filters")

    else:
        print("Unknown command")


# start app
if __name__ == "__main__":
    main_application()