def calculate_ecowas_vat(amount, country_code):
    """Applies standard VAT rates for West African (ECOWAS) countries."""
    rates = {'NG': 0.075, 'GH': 0.15, 'CI': 0.18, 'SN': 0.18}
    rate = rates.get(country_code.upper(), 0.0)
    return round(amount * rate, 2)