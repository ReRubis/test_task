from jh_interview.database.repository import (
    PostcodeRepository,
    TransactionRepository,
    PropertyRepository,
)
from jh_interview.models import (
    PostcodeModel,
    TransactionModel,
    PropertyModel
)
from jh_interview.database.schemas import (
    Postcode,
    Property,
    Transaction
)


class PropertyService:
    """Class to handle property operations."""

    def __init__(
        self,
        postcode_repository: PostcodeRepository,
        property_repository: PropertyRepository,
        transaction_repository: TransactionRepository,
    ):
        """Initialise the service."""
        self.postcode_repo = postcode_repository
        self.property_repo = property_repository
        self.transaction_repo = transaction_repository

    def return_properties_by_postcode(
        self,
        postcode: str,
    ) -> list[PropertyModel] | None:
        """Returns a list of properties by postcode."""
        properties = self.property_repo.get_properties_by_postcode(postcode)
        if properties is None:
            return None

        # Convert the sqlalchemy objects to dataclass models.
        properties = [
            PropertyModel(
                unique_id=property.unique_id,
                postcode=property.postcode,
                paon=property.paon,
                saon=property.saon,
                street=property.street,
                locality=property.locality,
                town_city=property.town_city,
                district=property.district,
                country=property.country,
                transactions=property.transactions,
            )
            for property in properties
        ]

        return properties

    def return_transaction(
        self,
        transaction_id: str,
    ) -> TransactionModel | None:
        """Returns transaction object by transaction id."""
        transaction = self.transaction_repo.get_transaction(transaction_id)
        if transaction is None:
            return None

        # Convert the sqlalchemy object to a dataclass model.
        transaction = TransactionModel(
            transaction_id=transaction.transaction_id,
            property_id=transaction.property_id,
            price=transaction.price,
            date_of_transfer=transaction.date_of_transfer,
        )

        return transaction

    def return_property_by_transaction(
        self,
        transaction_id: str,
    ) -> PropertyModel | None:
        """Returns property object to which the transaction is related."""
        transaction = self.transaction_repo.get_transaction(transaction_id)
        if transaction is None:
            return None

        property = self.property_repo.get_property(
            transaction.property_id)

        if property is None:
            return None

        # Convert the sqlalchemy object to a dataclass model.
        property = PropertyModel(
            unique_id=property.unique_id,
            postcode=property.postcode,
            paon=property.paon,
            saon=property.saon,
            street=property.street,
            locality=property.locality,
            town_city=property.town_city,
            district=property.district,
            country=property.country,
            transactions=property.transactions,
        )

        return property
