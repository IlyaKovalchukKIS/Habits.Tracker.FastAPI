from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from src.auth.database import fastapi_users
from src.repositories.crud.habit import HabitOrmCrud
from src.repositories.db_helper import db_helper
from src.repositories.models.user import UserOrm
from src.schemas import habit as habit_schemas
from src.validators.habit import HabitValidator

habit_routers = APIRouter(prefix="/habit", tags=["Habit"])

current_user = fastapi_users.current_user()


@habit_routers.post("/create/", response_model=habit_schemas.HabitRead)
async def create_habit(
    data: habit_schemas.HabitCreate = Depends(habit_schemas.HabitCreate),
    session: AsyncSession = Depends(db_helper.session_dependency),
    user: UserOrm = Depends(current_user),
):
    """Создание привычки"""
    related_habit = data.model_dump().get("related_habit", None)

    if related_habit:
        get_related_habit = await HabitOrmCrud.get_habit_by_id(session, related_habit)
        get_related_habit = get_related_habit.pleasant_habit
    else:
        get_related_habit = None
    validation = HabitValidator("related_habit", "award", "pleasant_habit").__call__(
        data.model_dump(), get_related_habit
    )
    if validation:
        return JSONResponse(status_code=400, content={"error": validation})
    return await HabitOrmCrud.insert_habit(session, data, user)


@habit_routers.get("/get/by/{habit_id}", response_model=habit_schemas.HabitRead)
async def get_habit_by_id(
    habit_id: int, session: AsyncSession = Depends(db_helper.session_dependency)
):
    """Получение привычки по id"""
    pass


@habit_routers.get(
    "/get/by/user/{user_id}/", response_model=List[habit_schemas.HabitRead]
)
async def get_habit_by_user_id(
    user_id: int, session: AsyncSession = Depends(db_helper.session_dependency)
):
    """Получение привычки по id пользователя"""
    pass


@habit_routers.get("/get/all/", response_model=List[habit_schemas.HabitRead])
async def get_all_habits(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    """Получение всех привычек"""
    pass


@habit_routers.get("/get/published/", response_model=List[habit_schemas.HabitRead])
async def get_published_habits(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    """Получение публичных привычек"""
    pass


@habit_routers.put("/update/", response_model=habit_schemas.HabitUpdate)
async def update_habit(
    data: dict, session: AsyncSession = Depends(db_helper.session_dependency)
):
    """Обновление привычки"""
    pass


@habit_routers.delete("/delete/")
async def delete_habit(
    habit_id: int, session: AsyncSession = Depends(db_helper.session_dependency)
):
    """Удаление привычки"""
    pass
