class TotalPrice:
    def __init__(self, currency: str):
        self.currency = currency

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if value is not None}
