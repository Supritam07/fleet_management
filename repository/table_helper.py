from config.db_config import Session, engine
from functools import lru_cache
from sqlalchemy import Table, MetaData
from sqlalchemy.util import memoized_property


@lru_cache()
class Tables:
    def __init__(self):
        self.metadata = MetaData()
        self.metadata.bind = engine

    @memoized_property
    def admin(self):
        return Table("user_type", self.metadata, autoload=True, autoload_with=engine)

@lru_cache()
def db_session():
    return Session()
