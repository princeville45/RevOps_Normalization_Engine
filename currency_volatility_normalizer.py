"""
RevOps Normalization Engine: Currency Volatility Normalizer
Vibe: Global Architect | Logic: Financial Stability

Revenue in volatile currencies (NGN) must be normalized to a hard currency (USD)
to reflect true Net Worth growth.
"""

def normalize_revenue(revenue_data, exchange_rate_history):
    """
    Converts local currency revenue to USD based on historical rates.
    """
    print("Normalizing Volatile Assets...")
    normalized_report = []
    
    for entry in revenue_data:
        date = entry['date']
        local_amount = entry['amount']
        rate = exchange_rate_history.get(date, 800) # Fallback rate
        
        usd_amount = local_amount / rate
        normalized_report.append({
            "date": date,
            "local": local_amount,
            "usd": round(usd_amount, 2)
        })
        
    return normalized_report

if __name__ == "__main__":
    data = [{"date": "2024-01", "amount": 1000000}, {"date": "2024-02", "amount": 1200000}]
    rates = {"2024-01": 850, "2024-02": 1100}
    
    report = normalize_revenue(data, rates)
    for r in report:
        print(f"Period: {r['date']} | USD Value: ${r['usd']}")
