# src/infrastructure/health.py
import asyncio
from sqlalchemy import text
from checkin_app.src.database.connection import engine

async def check_connection() -> bool:
    """
    Performs a lightweight async connection check.
    Verifies both the connection and the existence of the 'Events' schema.
    
    Returns:
        bool: True if the connection and schema check are successful, False otherwise.
    """
    try:
        async with engine.connect() as conn:
            # Basic connectivity
            await conn.execute(text("SELECT 1"))
            # Schema check
            await conn.execute(text('SELECT 1 FROM "Events".events LIMIT 1'))
            return True
    except Exception as e:
        print(f"Connection or Schema check failed: {e}")
        return False

if __name__ == "__main__":
    success = asyncio.run(check_connection())
    print(f"Database connection and schema successful: {success}")
