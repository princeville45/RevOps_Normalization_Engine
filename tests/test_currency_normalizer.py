import unittest

from currency_normalizer import normalize_currency


class NormalizeCurrencyTests(unittest.TestCase):
    def test_usd_amount_is_returned_unchanged(self):
        self.assertEqual(normalize_currency(125.5, "USD"), 125.5)

    def test_ngn_amount_uses_supplied_rate(self):
        self.assertEqual(normalize_currency(150000, "NGN", rate_ngn_to_usd=1500), 100)

    def test_currency_code_is_case_insensitive(self):
        self.assertEqual(normalize_currency(150000, "ngn", rate_ngn_to_usd=1500), 100)

    def test_unsupported_currency_raises_value_error(self):
        with self.assertRaises(ValueError):
            normalize_currency(100, "EUR")


if __name__ == "__main__":
    unittest.main()
