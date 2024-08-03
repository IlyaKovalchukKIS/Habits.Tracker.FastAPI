from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.db_helper import db_helper
from src.schemas import habit_schemas

habit_routers = APIRouter(prefix="/habit", tags=["Habit"])

depends = Depends(db_helper.session_dependency)


@habit_routers.post("/create/", response_model=habit_schemas.HabitCreate)
async def create_habit(data: dict, session: AsyncSession = depends):
    """Создание привычки"""
    pass


@habit_routers.get("/get/by/{habit_id}", response_model=habit_schemas.HabitRead)
async def get_habit_by_id(habit_id: int, session: AsyncSession = depends):
    """Получение привычки по id"""
    pass


@habit_routers.get(
    "/get/by/user/{user_id}/", response_model=List[habit_schemas.HabitRead]
)
async def get_habit_by_user_id(user_id: int, session: AsyncSession = depends):
    """Получение привычки по id пользователя"""
    pass


@habit_routers.get("/get/all/", response_model=List[habit_schemas.HabitRead])
async def get_all_habits(session: AsyncSession = depends):
    """Получение всех привычек"""
    pass


@habit_routers.get("/get/published/", response_model=List[habit_schemas.HabitRead])
async def get_published_habits(session: AsyncSession = depends):
    """Получение публичных привычек"""
    pass


@habit_routers.put("/update/", response_model=habit_schemas.HabitUpdate)
async def update_habit(data: dict, session: AsyncSession = depends):
    """Обновление привычки"""
    pass


@habit_routers.delete("/delete/")
async def delete_habit(habit_id: int, session: AsyncSession = depends):
    """Удаление привычки"""
    pass
