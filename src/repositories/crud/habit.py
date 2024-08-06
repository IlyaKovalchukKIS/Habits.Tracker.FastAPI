from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.models.habit import HabitOrm
from src.schemas import habit as schemas
from src.schemas.habit import HabitRead


class HabitOrmCrud:

    @staticmethod
    async def insert_habit(session: AsyncSession, data: schemas.HabitCreate, user):
        """Создание привычки"""
        data = data.model_dump()
        data["user_id"] = user.id  # user.id
        habit = HabitOrm(**data)
        session.add(habit)
        await session.commit()
        await session.refresh(habit)
        return habit

    @staticmethod
    async def get_habit_by_id(session: AsyncSession, habit_id: int):
        """Получение привычки по id"""
        return await session.get(HabitOrm, habit_id)

    @staticmethod
    async def get_habit_by_user_id(session: AsyncSession, user_id: int):
        """Получение привычки по id пользователя"""
        return await session.execute(
            select(HabitOrm).where(HabitOrm.user_id == user_id)
        )

    @staticmethod
    async def get_all_habits(session: AsyncSession):
        """Получение всех привычек"""
        pass

    @staticmethod
    async def get_published_habits(session: AsyncSession):
        """Получение публичных привычек"""
        pass

    @staticmethod
    async def update_habit(session: AsyncSession, data: dict):
        """Обновление привычки"""
        pass

    @staticmethod
    async def delete_habit(session: AsyncSession, habit_id: int):
        """Удаление привычки"""
        pass
