from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.db_helper import db_helper
from src.schemas import user as user_schemas

user_routers = APIRouter(prefix="/user", tags=["User"])


@user_routers.post("/create/", response_model=user_schemas.UserCreate)
async def create_user(session: AsyncSession = Depends(db_helper.session_dependency)):
    """Создание пользователя"""
    pass


@user_routers.get("/get/{user_id}/", response_model=user_schemas.UserRead)
async def get_user_by_id(
    user_id: int, session: AsyncSession = Depends(db_helper.session_dependency)
):
    """Получение пользователя по id"""
    pass


@user_routers.get("/get/email/{email}/", response_model=user_schemas.UserRead)
async def get_user_by_email(
    email: str, session: AsyncSession = Depends(db_helper.session_dependency)
):
    """Получение пользователя по email"""
    pass


@user_routers.get("/get/all/", response_model=List[user_schemas.UserRead])
async def get_all_users(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    """Получение всех пользователей"""
    pass


@user_routers.put("/update/", response_model=user_schemas.UserUpdate)
async def update_user(
    user_id: int,
    data: dict,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    """Oбновление пользователя"""
    pass


@user_routers.delete("/delete/")
async def delete_user(
    user_id: int, session: AsyncSession = Depends(db_helper.session_dependency)
):
    """Удаление пользователя"""
    pass
