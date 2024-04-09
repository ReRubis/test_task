from dataclasses import dataclass, field
from hashlib import md5


@dataclass(slots=True)
class TransactionModel:
    transaction_id: str
    property_id: str
    postcode: str
    price: float
    date_of_transfer: str


@dataclass(slots=True)
class PropertyModel:
    unique_id: str
    """Unique identifier for the property.

    The 'PAON' (Primary Addressable Object Name) and 'SAON' (Secondary Addressable Object Name)
    are typically stable identifiers for a property, as they represent the address of the property.
    However, they might not be unique across different streets or postcodes.
    So, we use the combination of 'PAON', 'SAON', and 'postcode' to create a unique identifier for the property.
    """

    postcode: str
    paon: str | None
    saon: str | None
    street: str
    locality: str
    town_city: str
    district: str
    country: str
    transactions: list[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.unique_id:
            unique_id = f'{self.paon} {self.saon} {self.postcode}'
            self.unique_id = md5(unique_id.encode()).hexdigest()

    def add_transaction(self, transaction: str):
        self.transactions.append(transaction)


@dataclass(slots=True)
class PostcodeModel:
    postcode: str
    properties: list[PropertyModel] = field(default_factory=list)

    def add_property(self, property: PropertyModel):
        self.properties.append(property)
