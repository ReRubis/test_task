from jh_interview.database.db_session import get_session
from jh_interview.database.repository import (
    PropertyRepository,
    TransactionRepository,
    PostcodeRepository,
)

from pytest import mark

from jh_interview.service.property import PropertyService


# This is an integrational test.
# It assumes that the populated database is running.
# The test checks if the property is returned by transaction.
@mark.parametrize(
    "transaction_id, expected_result", [
        ('{01EB45EF-630D-40F3-E063-4704A8C05FDE}', True),
        ('{01EB45F0-95FC-40F3-E063-4704A8C05FDE}', True),
        ('{01EB45EF-68B2-40F3-E063-4704A8C05FDE}', True),
        ('{11111111-6892-40F3-E063-4704A1230FDE}', False)
    ]
)
def test_return_property_by_transaction(
    transaction_id: str,
    expected_result: bool,
):
    """Test return property by transaction."""
    with get_session() as session:
        property_repository = PropertyRepository(session)
        transaction_repository = TransactionRepository(session)
        postcode_repository = PostcodeRepository(session)

        property_service = PropertyService(
            postcode_repository,
            property_repository,
            transaction_repository,
        )

        property = property_service.return_property_by_transaction(
            transaction_id
        )
        assert bool(property) == expected_result


@mark.parametrize(
    "postcode, expected_result", [
        ('ST10 4BS', 3),
    ]
)
def test_get_transactions_by_postcode(
    postcode: str,
    expected_result: list[str] | None,
):
    """Test get transactions by postcode."""
    with get_session() as session:
        property_repository = PropertyRepository(session)
        transaction_repository = TransactionRepository(session)
        postcode_repository = PostcodeRepository(session)

        property_service = PropertyService(
            postcode_repository,
            property_repository,
            transaction_repository,
        )

        properties = property_service.return_properties_by_postcode('ST10 4BS')

        transactions_id_list = []
        transactions = []

        for property in properties:
            transactions_id_list = transactions_id_list + property.transactions

        for id in transactions_id_list:
            transaction = property_service.return_transaction(id)
            transactions.append(transaction)

        assert len(transactions) == expected_result
