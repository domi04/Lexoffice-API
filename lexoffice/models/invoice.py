from typing import List

from .address import Address
from .lineItem import LineItem
from .totalPrice import TotalPrice
from .taxConditions import TaxConditions
from .shippingConditions import ShippingConditions


class Invoice:
    def __init__(
        self,
        voucherDate: str,
        address: Address,
        lineItems: List[LineItem],
        totalPrice: TotalPrice,
        taxConditions: TaxConditions,
        shippingConditions: ShippingConditions,
    ):
        self.voucherDate = voucherDate
        self.address = address
        self.lineItems = lineItems
        self.totalPrice = totalPrice
        self.taxConditions = taxConditions
        self.shippingConditions = shippingConditions

    def to_dict(self):
        return {
            "voucherDate": self.voucherDate,
            "address": self.address.to_dict(),
            "lineItems": [li.to_dict() for li in self.lineItems],
            "totalPrice": self.totalPrice.to_dict(),
            "taxConditions": self.taxConditions.to_dict(),
            "shippingConditions": self.shippingConditions.to_dict(),
        }
