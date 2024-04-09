import pytest
from jh_interview.models import PropertyModel, TransactionModel
import numpy as np
import pandas as pd
from pathlib import Path

from hashlib import md5


DATA_DIR = Path('./data/')
"""Path to the data directory."""

PP_COLUMN_NAMES = [
    'transaction_id', 'price', 'date_of_transfer', 'postcode', 'property_type',
    'old_new', 'duration', 'paon', 'saon', 'street', 'locality', 'town_city',
    'district', 'country', 'ppd_category_type', 'record_status'
]


@pytest.fixture
def transactions_df() -> pd.DataFrame:
    PRICE_PAID_FILE_FIRST = DATA_DIR / 'pp-2019.csv'
    PRICE_PAID_FILE_SECOND = DATA_DIR / 'pp-2020.csv'

    transactions_df = pd.concat(
        [
            pd.read_csv(
                PRICE_PAID_FILE_FIRST,
                names=PP_COLUMN_NAMES,
            ),
            pd.read_csv(
                PRICE_PAID_FILE_SECOND,
                names=PP_COLUMN_NAMES,
            )
        ]
    )
    return transactions_df


def check_property_equality(
    property: PropertyModel,
    other: PropertyModel
) -> bool:
    """
    Check if two properties are equal.
    """

    assert property.postcode == other.postcode
    assert property.paon == other.paon
    assert property.saon == other.saon
    assert property.street == other.street
    assert property.locality == other.locality
    assert property.town_city == other.town_city
    assert property.district == other.district
    assert property.country == other.country


def test_property_id(transactions_df: pd.DataFrame):
    """
    Property ID is combination of 'PAON', 'SAON', and 'Street'.

    Checks if the defined property ID is correct. 
    Creates a property object from every transaction.
    Compares the property object with the same IDs. 
    Fails if they differ.
    """
    properties: dict[str, PropertyModel] = {}

    for _, row in transactions_df.iterrows():
        property_id = f"{row['paon']}-|-{row['saon']}" \
            + f"-|-{row['country']}-|-{row['postcode']}" \
            + f"-|-{row['town_city']}-|-{row['street']}" \
            + f"-|-{row['locality']}-|-{row['district']}"
        property_id = md5(property_id.encode()).hexdigest()

        transaction = TransactionModel(
            transaction_id=row['transaction_id'],
            property_id=property_id,
            price=row['price'],
            date_of_transfer=row['date_of_transfer']
        )

        new_property = PropertyModel(
            unique_id=property_id,
            postcode=row['postcode'] if pd.notna(row['postcode']) else None,
            paon=row['paon'] if pd.notna(row['paon']) else None,
            saon=row['saon'] if pd.notna(row['saon']) else None,
            street=row['street'] if pd.notna(row['street']) else None,
            locality=row['locality'] if pd.notna(row['locality']) else None,
            town_city=row['town_city'] if pd.notna(row['town_city']) else None,
            district=row['district'] if pd.notna(row['district']) else None,
            country=row['country'] if pd.notna(row['country']) else None,
        )

        if property_id in properties:
            check_property_equality(properties[property_id], new_property)

        properties[property_id] = new_property

        properties[property_id].add_transaction(transaction)
