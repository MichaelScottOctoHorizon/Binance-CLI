from binance_cli import run_command
from io import StringIO
import sys


def test_info_command():

    captured = StringIO()
    sys.stdout = captured

    run_command("binance_cli info BTCUSDT")

    sys.stdout = sys.__stdout__

    output = captured.getvalue()

    assert "BTCUSDT" in output