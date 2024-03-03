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
        return {key: value for key, value in self.__dict__.items() if value is not None}
