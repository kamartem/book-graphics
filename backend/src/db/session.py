from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from core import config

engine = create_engine(config.DATABASE_URL)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
