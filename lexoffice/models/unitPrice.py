from typing import Optional


class UnitPrice:
    def __init__(
        self,
        currency: str,
        taxRatePercentage: int,
        netAmount: Optional[float] = None,
        grossAmount: Optional[float] = None,
    ):
        self.currency = currency
        self.netAmount = netAmount
        self.grossAmount = grossAmount
        self.taxRatePercentage = taxRatePercentage

    def to_dict(self):
        return {
            "currency": self.currency,
            "netAmount": self.netAmount,
            "grossAmount": self.grossAmount,
            "taxRatePercentage": self.taxRatePercentage,
        }
