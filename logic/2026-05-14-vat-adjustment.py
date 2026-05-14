def apply_vat_adjustment(amount, country_code):
    """Adjusts gross revenue to net revenue based on regional VAT rates."""
    vat_rates = {
        'NG': 0.075,
        'ZA': 0.15,
        'KE': 0.16,
        'GH': 0.15
    }
    rate = vat_rates.get(country_code, 0)
    net_revenue = amount / (1 + rate)
    return round(net_revenue, 2)