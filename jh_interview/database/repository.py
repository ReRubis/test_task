from datetime import datetime
from jh_interview.database.schemas import Transaction, Property, Postcode
from sqlalchemy.inspection import inspect
from sqlalchemy.orm.query import Query
from sqlalchemy.orm import Session


class BaseRepository():
    """
    A class that provides basic functionality for working with DB.
    """
    __model__ = None

    def __init__(self, session: Session):
        self.session = session

    def get(self, id):
        """Returns a content with a certain Id"""
        return self.query(self.__model__).get(id)

    def get_list(self) -> list:
        return self.query(self.__model__).all()

    def save(self, model):
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return model

    def delete(self, id):
        model = self.get(id)
        if not model:
            raise Exception('Model not found')
        self.query(self.__model__).filter_by(id=id).update(
            {'removed_at': datetime.now()}
        )
        return model

    def filter_dict(self, model, data):
        """
        Filters data dict based on the fields of a given SQLAlchemy model.

        Args:
            model: SQLAlchemy model class
            data (dict): Data to filter

        Returns:
            dict: Filtered data
        """
        inspector = inspect(model)
        fields = set([column.name for column in inspector.columns])
        return {key: value for key, value in data.items() if key in fields}

    @property
    def query(self) -> Query:
        """
        The decorator sets the query function as a class attribute.
        The function returns it so I don't have to pass the __model__
        every time one needs to query.
        """
        return self.session.query(self.__model__)


class TransactionRepository(BaseRepository):
    __model__ = Transaction


class PropertyRepository(BaseRepository):
    __model__ = Property


class PostcodeRepository(BaseRepository):
    __model__ = Postcode
