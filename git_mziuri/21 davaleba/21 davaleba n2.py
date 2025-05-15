class Currency:
    exchange_rates = {"GEL": 1, "USD": 2.7, "EUR": 3}

    def __init__(self, value, unit="GEL"):
        self.value = float(value)
        self.unit = unit.upper()
        if self.unit not in self.exchange_rates:
            raise ValueError("Unsupported currency unit")

    def __str__(self):
        return f"{self.value:.2f} {self.unit}"

    def changeTo(self, new_unit):
        new_unit = new_unit.upper()
        if new_unit not in self.exchange_rates:
            raise ValueError("Unsupported currency unit")
        gel_value = self.value * self.exchange_rates[self.unit]  # Convert to GEL
        new_value = gel_value / self.exchange_rates[new_unit]  # Convert to new currency
        return Currency(new_value, new_unit)

# Пример работы
usd = Currency(100, "USD")
eur = Currency(200, "EUR")
gel = Currency(300, "GEL")

print(usd)  # 100.00 USD
print(usd.changeTo("EUR"))
