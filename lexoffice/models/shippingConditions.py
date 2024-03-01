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
        return {
            "shippingType": self.shippingType,
            "shippingDate": self.shippingDate,
            "shippingEndDate": self.shippingEndDate,
        }
