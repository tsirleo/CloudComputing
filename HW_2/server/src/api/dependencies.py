from src.settings import Settings
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.pool import NullPool
from src.core.main import DatabaseManager


def get_database():
    settings = Settings()
    url = URL.create(
        settings.db_driver,
        username=settings.db_username,
        password=settings.db_password,
        host=settings.db_host,
        database=settings.db_name,
        port=settings.db_port,
    )
    engine = create_engine(url, poolclass=NullPool)
    engine.connect()

    return DatabaseManager(engine)
