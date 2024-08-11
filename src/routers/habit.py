from typing import List, Annotated

from attr import attrs
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from src.auth.database import fastapi_users
from src.repositories.crud.habit import HabitOrmCrud
from src.repositories.db_helper import db_helper
from src.repositories.models.habit import HabitOrm
from src.repositories.models.user import UserOrm
from src.schemas import habit as habit_schemas
from src.validators.habit import HabitValidator

habit_routers = APIRouter(prefix="/habit", tags=["Habit"])

current_user = fastapi_users.current_user()


@habit_routers.post("/create/", response_model=habit_schemas.HabitRead | dict)
async def create_habit(
    data: habit_schemas.HabitCreate = Depends(habit_schemas.HabitCreate),
    session: AsyncSession = Depends(db_helper.session_dependency),
    user: UserOrm = Depends(current_user),
):
    """Создание привычки"""
    try:
        related_habit = None
        if data.related_habit:
            related_habit = await HabitOrmCrud.get_habit_by_id(
                session, data.related_habit, user.id
            )
            if related_habit is None:
                raise ValueError("Привычка не найдена")
        await HabitValidator()(data, related_habit, user.id)
    except ValueError as e:
        return {"ValidationError": str(e)}
    return await HabitOrmCrud.insert_habit(session, data, user.id)


@habit_routers.get("/get/{habit_id}", response_model=habit_schemas.HabitRead)
async def get_habit_by_id(
    habit_id: int,
    session: AsyncSession = Depends(db_helper.session_dependency),
    user: UserOrm = Depends(current_user),
):
    """Получение привычки по id"""
    return await HabitOrmCrud.get_habit_by_id(session, habit_id, user.id)


@habit_routers.get("/get/all/", response_model=List[habit_schemas.HabitRead])
async def get_habit_by_user_id(
    user: UserOrm = Depends(current_user),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    """Получение привычки по id пользователя"""
    get_all_habit = await HabitOrmCrud.get_habit_by_user_id(session, user.id)
    for habit in get_all_habit:
        if habit.related_habit:
            relation_habit = await HabitOrmCrud.get_habit_by_id(
                session, habit.related_habit, user.id
            )
            habit.related_habit = [relation_habit]
    return get_all_habit


@habit_routers.get("/get/published/", response_model=List[habit_schemas.HabitRead])
async def get_published_habits(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    """Получение публичных привычек"""
    result = await HabitOrmCrud.get_published_habits(session)
    return result


@habit_routers.patch("/update/", response_model=habit_schemas.HabitRead | dict)
async def update_habit(
    habit_update: Annotated[habit_schemas.HabitCreate, Depends()],
    habit_id: int,
    session: AsyncSession = Depends(db_helper.session_dependency),
    user: UserOrm = Depends(current_user),
):
    """Обновление привычки"""
    # habit = await HabitOrmCrud.get_habit_by_id(session, habit_id, user.id)
    # validation = await HabitValidator(
    #     related_habit="related_habit", award="award", pleasant_habit="pleasant_habit"
    # )(data=habit_update.model_dump(), user=user, session=session)
    # if validation:
    #     return {"error": validation}
    # print("return")
    # return await HabitOrmCrud.update_habit(session, habit, habit_update.__dict__)
    pass


@habit_routers.delete("/delete/")
async def delete_habit(
    habit_id: int,
    session: AsyncSession = Depends(db_helper.session_dependency),
    user: UserOrm = Depends(current_user),
):
    """Удаление привычки"""
    return await HabitOrmCrud.delete_habit(session, habit_id, user.id)
