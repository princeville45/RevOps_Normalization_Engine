"""
Multi-Currency Revenue Normalization Engine
Author: Irem Victor Chinonso | Statistical Business Architect
Date: 2026-05-12
Repo: RevOps-Normalization-Engine

Normalizes revenue streams across multiple currencies
into a single reporting base (NGN + USD).
Handles FX rate volatility, weighted conversion,
and statistical outlier detection on FX-adjusted revenue.
"""

import pandas as pd
import numpy as np
from datetime import datetime


# Simulated FX rates relative to NGN (May 2026)
FX_RATES_TO_NGN = {
    "NGN": 1.0,
    "USD": 1580.0,
    "GBP": 2020.0,
    "EUR": 1720.0,
    "GHS": 108.0,
    "KES": 12.3,
}


def generate_revenue_records(n=80):
    """Generate multi-currency revenue records."""
    np.random.seed(55)
    currencies = list(FX_RATES_TO_NGN.keys())
    records = []

    for i in range(n):
        currency = np.random.choice(currencies, p=[0.40, 0.30, 0.10, 0.10, 0.05, 0.05])
        if currency == "NGN":
            amount = round(np.random.uniform(5000, 500000), 2)
        elif currency == "USD":
            amount = round(np.random.uniform(10, 800), 2)
        elif currency in ("GBP", "EUR"):
            amount = round(np.random.uniform(5, 600), 2)
        else:
            amount = round(np.random.uniform(50, 3000), 2)

        records.append({
            "transaction_id": f"TXN-{i+1:04d}",
            "currency": currency,
            "original_amount": amount,
            "source": np.random.choice(["Salary", "Crypto", "Freelance", "YouTube", "Airdrop"]),
            "date": f"2026-05-{np.random.randint(1, 13):02d}"
        })

    return pd.DataFrame(records)


def normalize_to_ngn(df, fx_rates):
    """Convert all amounts to NGN using FX rates."""
    df = df.copy()
    df["fx_rate"] = df["currency"].map(fx_rates)
    df["amount_ngn"] = (df["original_amount"] * df["fx_rate"]).round(2)
    df["amount_usd"] = (df["amount_ngn"] / fx_rates["USD"]).round(4)
    return df


def detect_outliers_iqr(df, column="amount_ngn"):
    """Flag statistical outliers using IQR method."""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df = df.copy()
    df["outlier_flag"] = (df[column] < lower) | (df[column] > upper)
    return df, lower, upper


def revenue_by_source(df):
    """Aggregate normalized revenue by income source."""
    return df.groupby("source").agg(
        total_ngn=("amount_ngn", "sum"),
        total_usd=("amount_usd", "sum"),
        transactions=("transaction_id", "count"),
        avg_ngn=("amount_ngn", "mean")
    ).round(2).sort_values("total_ngn", ascending=False)


def revenue_by_currency(df):
    """Summarize original volume and NGN-equivalent by currency."""
    return df.groupby("currency").agg(
        transactions=("transaction_id", "count"),
        original_total=("original_amount", "sum"),
        ngn_equivalent=("amount_ngn", "sum")
    ).round(2)


def run_normalization():
    print("=" * 60)
    print("MULTI-CURRENCY REVENUE NORMALIZATION ENGINE")
    print("RevOps Normalization Engine | Irem Victor Chinonso")
    print("=" * 60)

    df = generate_revenue_records(80)
    df_norm = normalize_to_ngn(df, FX_RATES_TO_NGN)
    df_flagged, lower, upper = detect_outliers_iqr(df_norm)

    total_ngn = df_norm["amount_ngn"].sum()
    total_usd = df_norm["amount_usd"].sum()

    print(f"\nRecords Processed: {len(df_norm)}")
    print(f"Total Revenue (NGN): ₦{total_ngn:,.2f}")
    print(f"Total Revenue (USD): ${total_usd:,.2f}")

    print("\n--- REVENUE BY SOURCE ---")
    print(revenue_by_source(df_norm).to_string())

    print("\n--- REVENUE BY CURRENCY ---")
    print(revenue_by_currency(df_norm).to_string())

    outliers = df_flagged[df_flagged["outlier_flag"]]
    print(f"\n--- OUTLIER DETECTION (IQR Method) ---")
    print(f"Normal Range: ₦{lower:,.0f} — ₦{upper:,.0f}")
    print(f"Flagged Outliers: {len(outliers)} transactions")
    if not outliers.empty:
        print(outliers[["transaction_id", "currency", "original_amount", "amount_ngn", "source"]].to_string(index=False))

    print("\nNormalization complete.")


if __name__ == "__main__":
    run_normalization()
