from dataclasses import dataclass, field


@dataclass(slots=True)
class TransactionModel:
    transaction_id: str
    property_id: str
    price: float
    date_of_transfer: str


@dataclass(slots=True)
class PropertyModel:
    id: str
    """Unique identifier for the property.

    The 'PAON' (Primary Addressable Object Name) and 'SAON' (Secondary Addressable Object Name)
    are typically stable identifiers for a property, as they represent the address of the property.
    However, they might not be unique across different streets or postcodes.
    So, we use the combination of 'PAON', 'SAON', and 'Street' to create a unique identifier for the property.
    """

    property_type: str
    old_new: str
    postcode: str
    paon: str | None
    saon: str | None
    street: str
    locality: str
    town_city: str
    district: str
    country: str
    transactions: list[TransactionModel] = field(default_factory=list)

    def __post_init__(self):
        if not self.id:
            self.id = f'{self.paon}-{self.saon}-{self.street}'

    def add_transaction(self, transaction: TransactionModel):
        self.transactions.append(transaction)


@dataclass(slots=True)
class PostcodeModel:
    postcode: str
    properties: list[PropertyModel] = field(default_factory=list)

    def add_property(self, property: PropertyModel):
        self.properties.append(property)
