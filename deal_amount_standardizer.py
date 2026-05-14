def standardize_amount(amount_str):
    """
    Standardizes HubSpot deal amounts from various string formats to float.
    Handles commas, currency symbols, and whitespace.
    """
    if not amount_str: return 0.0
    clean_str = amount_str.replace(',', '').replace('$', '').replace('₦', '').strip()
    try:
        return float(clean_str)
    except ValueError:
        return 0.0

if __name__ == "__main__":
    print(standardize_amount("₦1,200,000.50"))
