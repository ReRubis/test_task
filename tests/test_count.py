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
    "years, expected_result", [
        (['2019', '2020'], {'M15': 790, 'E14': 556,
         'E16': 373, 'M4': 213, 'S3': 207}),
    ]
)
def test_get_transactions_count_by_postcode_and_year(
    years: list[str],
    expected_result: dict[str, dict[str, int]],
):
    """Test get transactions count by postcode and year."""
    with get_session() as session:
        property_repository = PropertyRepository(session)
        transaction_repository = TransactionRepository(session)
        postcode_repository = PostcodeRepository(session)

        property_service = PropertyService(
            postcode_repository,
            property_repository,
            transaction_repository,
        )

        result = property_service.return_highest_increase_postcodes(
            years=years
        )

    assert result == expected_result
