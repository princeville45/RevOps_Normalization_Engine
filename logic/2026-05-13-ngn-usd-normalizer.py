class RevenueNormalizer:
    def __init__(self, rates): self.rates = rates
    def normalize(self, amount, currency, target="USD"):
        return amount * (self.rates.get(target) / self.rates.get(currency))