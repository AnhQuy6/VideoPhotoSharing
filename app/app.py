from fastapi import FastAPI, HTTPException, File, UploadFile, Depends, HTTPException, Form
from app.schemas import PostCreate, PostRespose
from app.db import Post, create_db_and_tables, get_async_session
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from contextlib import asynccontextmanager
from sqlalchemy import select

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield
app = FastAPI(lifespan=lifespan)

@app.post("/upload")
async def upload_file(
        file: UploadFile = File(...),
        caption: str = Form(""),
        session: AsyncSession = Depends(get_async_session),
):
    post = Post(
        caption=caption,
        url="dummuurl",
        file_type="photo",
        file_name="dummy name"
    )
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post

@app.get("/feed")
async def get_feed(
        session: AsyncSession = Depends(get_async_session)
):
    return await session.execute(select(Post).order_by(Post.created_at.desc()))
