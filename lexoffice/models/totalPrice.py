class TotalPrice:
    def __init__(self, currency: str):
        self.currency = currency

    def to_dict(self):
        return {"currency": self.currency}
