def format_fundamentals(fund):
    """
    Formats large numbers and percentages for UI display
    """
    formatted = {}

    for k, v in fund.items():
        if isinstance(v, float):
            if abs(v) < 1:
                formatted[k] = f"{v:.2%}"
            else:
                formatted[k] = round(v, 2)
        elif isinstance(v, int):
            formatted[k] = f"{v:,}"
        else:
            formatted[k] = v

    return formatted