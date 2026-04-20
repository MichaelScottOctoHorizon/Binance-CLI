from typing import Dict, Any
from sub_programs.models import Symbol

def extract_filters(symbol: dict):

    result = {
        "symbol": symbol.get("symbol"),   # ✅ ADD THIS
        "status": symbol.get("status"),
        "tick_size": None,
        "min_qty": None,
        "step_size": None,
    }

    filters = symbol.get("filters", [])

    for f in filters:
        if f["filterType"] == "PRICE_FILTER":
            result["tick_size"] = f.get("tickSize")

        if f["filterType"] == "LOT_SIZE":
            result["min_qty"] = f.get("minQty")
            result["step_size"] = f.get("stepSize")

    return result