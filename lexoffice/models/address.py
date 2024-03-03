from typing import Optional


class Address:
    """Address of a contact or a company. When the contactId is given, the rest is probably provided by Lexoffice. Need to test this."""

    def __init__(
        self,
        contactId: Optional[str] = None,
        name: Optional[str] = None,
        supplement: Optional[str] = None,
        street: Optional[str] = None,
        city: Optional[str] = None,
        zip: Optional[int] = None,
        countryCode: Optional[str] = None,
    ):
        self.contactId = contactId
        self.name = name
        self.supplement = supplement
        self.street = street
        self.city = city
        self.zip = zip
        self.countryCode = countryCode

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if value is not None}
