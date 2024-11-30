from os import getenv

from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from sqlalchemy.pool import QueuePool

load_dotenv()
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote_plus


DATABASE_URL = f"{getenv('DB_DRIVER')}{getenv('DB_USER')}:{quote_plus(getenv('DB_PASS'))}@{getenv('DB_HOST')}:{getenv('DB_PORT')}/{getenv('DB_NAME')}"
engine = create_engine(DATABASE_URL, poolclass=QueuePool, pool_size=int(getenv('POOL_SIZE')),
                       max_overflow=int(getenv('MAX_POOL_SIZE')),
                       connect_args={'options': '-csearch_path={}'.format(str(getenv('SCHEMA')))}, echo=False)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
