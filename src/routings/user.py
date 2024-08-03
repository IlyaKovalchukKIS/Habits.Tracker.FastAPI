from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.db_helper import db_helper

user_routers = APIRouter(prefix="/user", tags=["User"])

depends_session: AsyncSession = Depends(db_helper.session_dependency)


@user_routers.post("/create/")
async def create_user(session: depends_session):
    """Создание пользователя"""
    pass


@user_routers.get("/get/")
async def get_user_by_id(user_id: int, session: AsyncSession = depends_session):
    """Получение пользователя по id"""
    pass


@user_routers.get("get/by/email")
async def get_user_by_email(session: AsyncSession, email: str):
    """Получение пользователя по email"""
    pass


@user_routers.get("/get/by/email/")
async def get_user_by_email(email: str, session: AsyncSession = depends_session):
    """Получение пользователя по email"""
    pass


@user_routers.get("/get/all/")
async def get_all_users(session: AsyncSession = depends_session):
    """Получение всех пользователей"""
    pass


@user_routers.put("/update/")
async def update_user(
    user_id: int, data: dict, session: AsyncSession = depends_session
):
    """Oбновление пользователя"""
    pass


@user_routers.delete("/delete/")
async def delete_user(user_id: int, session: AsyncSession = depends_session):
    """Удаление пользователя"""
    pass
