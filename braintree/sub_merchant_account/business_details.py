from braintree.attribute_getter import AttributeGetter
from braintree.sub_merchant_account.address_details import AddressDetails

class BusinessDetails(AttributeGetter):
    detail_list = [
        "legal_name",
        "registered_as",
        "address_details",
    ]

    def __init__(self, attributes):
        AttributeGetter.__init__(self, attributes)
        self.address_details = AddressDetails(attributes.get("address", {}))

    def __repr__(self):
        return super(BusinessDetails, self).__repr__(self.detail_list)
