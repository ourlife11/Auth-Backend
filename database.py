import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 1. Get the URL from the environment
DATABASE_URL = os.getenv("DATABASE_URL")

# 2. Fix the prefix if necessary (SQLAlchemy 2.0 compatibility)
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# 3. Use SQLite ONLY if no DATABASE_URL is found (usually local dev)
if not DATABASE_URL:
    DATABASE_URL = "sqlite:///./auth.db"

# 4. Create the engine
# Note: connect_args is only needed for SQLite
if "sqlite" in DATABASE_URL:
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine)