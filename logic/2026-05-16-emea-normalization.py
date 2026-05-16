def normalize_to_usd(amount, currency, rates_map):
    """Normalizes EMEA regional revenues to USD for unified reporting."""
    rate = rates_map.get(currency.upper(), 1.0)
    return round(amount / rate, 2)