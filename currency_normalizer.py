def normalize_currency(amount, currency, rate_ngn_to_usd=1500):
    """
    Normalizes revenue to USD for global reporting.
    Supports NGN to USD conversion using the Financial Pivot Law logic.
    """
    if currency.upper() == 'USD':
        return amount
    elif currency.upper() == 'NGN':
        return amount / rate_ngn_to_usd
    else:
        raise ValueError("Unsupported currency for normalization")

if __name__ == "__main__":
    print(f"1,500,000 NGN in USD: ${normalize_currency(1500000, 'NGN')}")
