# src/infrastructure/database.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from checkin_app.src.database.config import config

# Create the async engine
# Use connect_args to handle SSL for Supabase/PostgreSQL
engine = create_async_engine(
    config.connection_url, echo=False, future=True, connect_args={"ssl": "require"}
)

# Create the session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


async def get_async_session():
    """
    Dependency that provides an async database session.

    Returns:
        AsyncSession: A new SQLAlchemy async session.
    """
    async with AsyncSessionLocal() as session:
        async with session.begin():
            yield session


