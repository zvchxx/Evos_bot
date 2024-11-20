import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

from main.config import DB_USER, DB_NAME, DB_HOST, DB_PASS, DB_PORT

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

database = databases.Database(DATABASE_URL)

Base = declarative_base()
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)