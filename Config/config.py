#!/usr/bin/python
from configparser import ConfigParser
import urllib.parse
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker


def config(filename: str = 'database.ini', section: str = 'postgresql') -> str:
    """Parsing database parameters."""

    # Creating a parser.
    parser = ConfigParser()

    # Reading the config file.
    parser.read('./Config/'+filename)
    
    # Parsing the config file and returning parameters.
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return "postgresql+asyncpg://" + db['user'] + ':' + urllib.parse.quote_plus(db['password']) + '@' + db['host'] + '/' + db['database']

params = config()
engine = create_async_engine(params, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()