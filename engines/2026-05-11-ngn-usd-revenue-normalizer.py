import requests

def normalize_revenue_ngn_to_usd(revenue_data, exchange_rate=None):
    """
    Normalizes NGN revenue to USD.
    revenue_data: list of dicts with 'period', 'amount_ngn'
    exchange_rate: optional fixed rate, else fetches from exchangerate-api
    """
    if exchange_rate is None:
        try:
            # Fallback to a realistic fixed rate if API fails
            response = requests.get("https://open.er-api.com/v6/latest/USD")
            rates = response.json().get('rates', {})
            exchange_rate = rates.get('NGN', 1500) 
        except:
            exchange_rate = 1500
            
    normalized_data = []
    for entry in revenue_data:
        amount_usd = entry['amount_ngn'] / exchange_rate
        normalized_data.append({
            "period": entry['period'],
            "amount_ngn": entry['amount_ngn'],
            "amount_usd": round(amount_usd, 2),
            "rate_used": exchange_rate
        })
        
    return normalized_data

if __name__ == "__main__":
    # Sample quarterly revenue in Nigerian Naira
    ngn_revenue = [
        {"period": "Q1 2026", "amount_ngn": 5000000},
        {"period": "Q2 2026", "amount_ngn": 7500000},
    ]
    
    normalized = normalize_revenue_ngn_to_usd(ngn_revenue)
    print("--- NGN to USD Revenue Normalization ---")
    for row in normalized:
        print(f"Period: {row['period']} | NGN: {row['amount_ngn']:,} | USD: {row['amount_usd']:,} (Rate: {row['rate_used']})")
