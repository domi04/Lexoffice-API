from .unitPrice import UnitPrice
from typing import Optional


class LineItem:
    def __init__(
        self,
        name: str,
        quantity: Optional[int],
        unitName: Optional[str],
        unitPrice: Optional[UnitPrice],
    ):
        self.type: str = (
            "custom"  # Supported values are custom, material, service and text.
        )
        self.name = name
        self.quantity = quantity  # Required for type custom, service and material.
        self.unitName = unitName  # Required for type custom, service and material.
        self.unitPrice = unitPrice  # Required for type custom, service and material.

    def to_dict(self):
        return {
            "type": self.type,
            "name": self.name,
            "quantity": self.quantity,
            "unitName": self.unitName,
            "unitPrice": self.unitPrice.to_dict(),
        }
