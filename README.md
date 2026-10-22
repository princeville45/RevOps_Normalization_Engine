# Revenue Normalization Engine

A small Python project for practising revenue data normalization across currencies. It currently includes simple conversion helpers and a revenue normalization class with configurable master currency and a small illustrative exchange-rate table.

## Current functionality

- Convert an amount from NGN to USD using a caller-supplied NGN-per-USD rate (or the function's demo default).
- Return USD amounts unchanged in the simple helper.
- Normalize supported currencies in `NormalizationEngine` using its configured rates.
- Calculate a units-per-day velocity index, returning zero when the number of days is zero or negative.

## Quick start

Requires Python 3. No third-party package is required for the current helper scripts.

```bash
python currency_normalizer.py
```

Example usage:

```python
from currency_normalizer import normalize_currency

usd_amount = normalize_currency(150000, "NGN", rate_ngn_to_usd=1500)
print(usd_amount)  # 100.0
```

Run the automated tests with Python's standard test runner:

```bash
python -m unittest discover -s tests -v
```

## Important limitations

- The exchange rates in the source code are illustrative defaults, not live market rates. Supply a verified rate for the relevant reporting date before using a conversion in real business decisions.
- The current implementation supports only the currencies explicitly configured in each helper.
- This repository is a learning project. It does not yet include a live exchange-rate provider, historical rate storage, financial rounding policy, or integration with a CRM.
- The tests cover the currently documented helper behavior; they do not establish production readiness.

## Planned improvements

1. Validate numeric amounts and exchange rates.
2. Define an explicit base-currency and rate-direction convention.
3. Add date-aware rates and a source for rate provenance.
4. Add tests for invalid inputs and supported currency pairs.
5. Add a reproducible sample dataset and example report.

## Author

Irem Victor Chinonso — Statistics student building practical skills in Python, data quality, and Revenue Operations.

