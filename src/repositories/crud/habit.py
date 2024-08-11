from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.models.habit import HabitOrm
from src.schemas import habit as schemas
from src.schemas.habit import HabitRead


class HabitOrmCrud:

    @staticmethod
    async def insert_habit(session: AsyncSession, data: schemas.HabitCreate, user: int):
        """Создание привычки"""
        data = data.model_dump()
        data["user_id"] = user  # user.id
        habit = HabitOrm(**data)
        session.add(habit)
        await session.commit()
        await session.refresh(habit)
        return habit

    @staticmethod
    async def get_habit_by_id(session: AsyncSession, habit_id: int, user_id: int):
        """Получение привычки по id"""
        result = await session.execute(
            select(HabitOrm)
            .where(HabitOrm.id == habit_id)
            .where(HabitOrm.user_id == user_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_habit_by_user_id(session: AsyncSession, user_id: int):
        """Получение привычки по id пользователя"""
        result = await session.execute(
            select(HabitOrm).where(HabitOrm.user_id == user_id)
        )
        return result.scalars().all()

    # @staticmethod
    # async def get_all_habits(session: AsyncSession):
    #     """Получение всех привычек"""
    #     pass

    @staticmethod
    async def get_published_habits(session: AsyncSession):
        """Получение публичных привычек"""
        stmt = select(HabitOrm).where(HabitOrm.is_published == True)
        result: Result = await session.execute(stmt)
        return list(result.scalars().all())

    @staticmethod
    async def update_habit(session: AsyncSession, habit: HabitOrm, habit_update: dict):
        """Обновление привычки"""
        for key, value in habit_update.items():
            setattr(habit, key, value)
        session.add(habit)
        await session.commit()
        await session.refresh(habit)
        return habit

    @staticmethod
    async def delete_habit(session: AsyncSession, habit_id: int, user_id: int):
        """Удаление привычки"""
        result = await session.get(HabitOrm, habit_id)
        if result is not None:
            if result.user_id == user_id:
                await session.delete(result)
                await session.commit()
                return {"detail": "Success delete task"}
            return {"detail": "User is not owner to task"}
        return {"detail": f"There is no task with this number {habit_id} in the table"}
