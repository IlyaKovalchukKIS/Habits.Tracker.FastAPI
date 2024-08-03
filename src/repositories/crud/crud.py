from sqlalchemy.ext.asyncio import AsyncSession


class HabitOrmCrud:

    @staticmethod
    async def insert_habit(session: AsyncSession, data: dict):
        """Создание привычки"""
        pass

    @staticmethod
    async def get_habit_by_id(session: AsyncSession, habit_id: int):
        """Получение привычки по id"""
        pass

    @staticmethod
    async def get_habit_by_user_id(session: AsyncSession, user_id: int):
        """Получение привычки по id пользователя"""
        pass

    @staticmethod
    async def get_all_habits(session: AsyncSession):
        """Получение всех привычек"""
        pass

    @staticmethod
    async def get_published_habits(session: AsyncSession):
        """Получение публичных привычек"""
        pass
