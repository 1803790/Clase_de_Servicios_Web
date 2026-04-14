from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

database_url = "postgresql://admiin:admin@localhost/dbname"
engine = create_engine(database_url)

Base = declarative_base(engine)

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)