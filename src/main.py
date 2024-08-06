import uvicorn
from fastapi import FastAPI

from src.auth.database import fastapi_users, auth_backend
from src.auth.schemas import UserRead, UserCreate
from src.repositories.db_helper import db_helper, Base
from src.routers import habit, user

app = FastAPI()


app.include_router(habit.habit_routers)
app.include_router(user.user_routers)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)


async def create_table():
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True, port=8000)
