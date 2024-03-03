from typing import Optional


class ShippingConditions:
    def __init__(
        self,
        shippingType: str,
        shippingDate: Optional[str] = None,
        shippingEndDate: Optional[str] = None,
    ):
        self.shippingType = shippingType
        self.shippingDate = shippingDate
        self.shippingEndDate = shippingEndDate

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if value is not None}
