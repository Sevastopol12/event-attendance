# src/infrastructure/config.py
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class DatabaseConfig:
    """
    Database configuration loaded from environment variables.
    """
    user: str = os.getenv("user", "postgres")
    password: str = os.getenv("password", "")
    host: str = os.getenv("host", "localhost")
    port: str = os.getenv("port", "5432")
    dbname: str = os.getenv("dbname", "postgres")
    
    @property
    def connection_url(self) -> str:
        """
        Constructs the async SQLAlchemy connection URL.
        
        Returns:
            str: The formatted connection string.
        """
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"

config = DatabaseConfig()
