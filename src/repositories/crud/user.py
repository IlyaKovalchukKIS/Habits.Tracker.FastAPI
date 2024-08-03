from sqlalchemy.ext.asyncio import AsyncSession


class UserOrmCrud:

    @staticmethod
    async def insert_user(session: AsyncSession, data: dict):
        """Создание пользователя"""
        pass

    @staticmethod
    async def get_user_by_id(session: AsyncSession, user_id: int):
        """Получение пользователя по id"""
        pass

    @staticmethod
    async def get_user_by_email(session: AsyncSession, email: str):
        """Получение пользователя по email"""
        pass

    @staticmethod
    async def get_all_users(session: AsyncSession):
        """Получение всех пользователей"""
        pass

    @staticmethod
    async def update_user(session: AsyncSession, user_id: int, data: dict):
        """Oбновление пользователя"""
        pass

    @staticmethod
    async def delete_user(session: AsyncSession, user_id: int):
        """Удаление пользователя"""
        pass
