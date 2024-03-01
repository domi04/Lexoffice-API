class TaxConditions:
    def __init__(self, taxType: str):
        self.taxType = taxType  # Supported values are: gross, net, vatfree, intraCommunitySupply, constructionService13b, externalService13b, thirdPartyCountryService, thirdPartyCountryDelivery.

    def to_dict(self):
        return {"taxType": self.taxType}
