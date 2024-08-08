from typing import List, Annotated

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

    related_habit_id = data.model_dump().get("related_habit")
    related_habit = (
        await HabitOrmCrud.get_habit_by_id(session, related_habit_id)
        if related_habit_id
        else False
    )
    print(related_habit)
    pleasant_habit = related_habit.pleasant_habit if related_habit else None
    print(pleasant_habit)

    validation = HabitValidator("related_habit", "award", "pleasant_habit")(
        data.model_dump(), pleasant_habit
    )

    if validation:
        return JSONResponse(status_code=400, content={"error": validation})

    return await HabitOrmCrud.insert_habit(session, data, user)


@habit_routers.get("/get/by/{habit_id}", response_model=habit_schemas.HabitRead)
async def get_habit_by_id(
    habit_id: int, session: AsyncSession = Depends(db_helper.session_dependency)
):
    """Получение привычки по id"""
    return await HabitOrmCrud.get_habit_by_id(session, habit_id)


@habit_routers.get("/get/by/user/", response_model=List[habit_schemas.HabitRead])
async def get_habit_by_user_id(
    user: UserOrm = Depends(current_user),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    """Получение привычки по id пользователя"""
    return await HabitOrmCrud.get_habit_by_user_id(session, user.id)


# @habit_routers.get("/get/all/", response_model=List[habit_schemas.HabitRead])
# async def get_all_habits(
#     session: AsyncSession = Depends(db_helper.session_dependency),
# ):
#     """Получение всех привычек"""
#     pass


@habit_routers.get("/get/published/", response_model=List[habit_schemas.HabitRead])
async def get_published_habits(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    """Получение публичных привычек"""
    return await HabitOrmCrud.get_published_habits(session)


@habit_routers.put("/update/", response_model=habit_schemas.HabitUpdate)
async def update_habit(
    habit_update: Annotated[habit_schemas.HabitCreate, Depends()],
    habit_id: int,
    session: AsyncSession = Depends(db_helper.session_dependency),
    user: UserOrm = Depends(current_user),
):
    """Обновление привычки"""
    habit = await HabitOrmCrud.get_habit_by_id(session, habit_id)
    result = await HabitOrmCrud.update_habit(session, habit, habit_update.model_dump())
    return result


@habit_routers.delete("/delete/")
async def delete_habit(
    habit_id: int, session: AsyncSession = Depends(db_helper.session_dependency)
):
    """Удаление привычки"""
    pass
