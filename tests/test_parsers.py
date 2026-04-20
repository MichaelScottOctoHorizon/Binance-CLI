def extract_filters(data: dict):
    symbol = data["symbols"][0]   # ✅ unwrap list

    result = {
        "symbol": symbol.get("symbol"),
        "status": symbol.get("status"),
        "tick_size": None,
        "min_qty": None,
        "step_size": None,
    }

    for f in symbol.get("filters", []):
        if f["filterType"] == "PRICE_FILTER":
            result["tick_size"] = f.get("tickSize")

        elif f["filterType"] == "LOT_SIZE":
            result["min_qty"] = f.get("minQty")
            result["step_size"] = f.get("stepSize")

    return result