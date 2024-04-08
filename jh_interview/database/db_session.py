from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
from jh_interview.database.schemas import Base

MSSQL_LINK = 'mssql+pyodbc://sa:YourStrong!Passw0rd@localhost:1433/property_db?driver=ODBC+Driver+17+for+SQL+Server'
if not MSSQL_LINK:
    raise EnvironmentError(
        "Environment variable POSTGRES_DATABASE_URL is not set or is empty")
engine = create_engine(
    MSSQL_LINK
)
LocalSession = sessionmaker(bind=engine)


@contextmanager
def get_session():
    db = LocalSession()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def DB_init():
    Base.metadata.create_all(engine)
