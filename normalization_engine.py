import math
class NormalizationEngine:
    """EMEA Revenue Normalization Engine | Architect: Irem Victor Chinonso"""
    def __init__(self, master_currency="USD"):
        self.master_currency = master_currency
        self.exchange_rates = {"NGN": 1500.0, "GHS": 14.5, "KES": 130.0, "ZAR": 18.5}
    def normalize_revenue(self, amount, currency):
        if currency == self.master_currency: return amount
        rate = self.exchange_rates.get(currency)
        if not rate: raise ValueError(f"Currency {currency} not supported.")
        return round(amount / rate, 2)
    def calculate_velocity_index(self, units, days):
        return round(units / days, 2) if days > 0 else 0
