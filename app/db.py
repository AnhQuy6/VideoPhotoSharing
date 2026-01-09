import os
from collections.abc import AsyncGenerator
import uuid

from sqlalchemy import create_engine, engine
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_engine_from_config, async_sessionmaker
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, Text, String, DateTime, ForeignKey
from datetime import datetime

DATABASE_URL = "postgresql+asyncpg://postgres:2112@localhost:5432/postgres"

class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    caption = Column(Text)
    url = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with get_async_session() as session:
        yield session