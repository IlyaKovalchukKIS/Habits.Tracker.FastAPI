from typing import Annotated

from sqlalchemy import String
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, mapped_column

from src.config.config import settings

str_40 = Annotated[str, mapped_column(String(40))]


class Base(DeclarativeBase):
    pass


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        """
        Класс помощник для работы с подключением к базе данных

        :param url: url базы данных указанный в конфиге проекта
        :param echo: вывод в консоль запросов к базе данных
        """
        # Создание движка
        self.engine = create_async_engine(url=url, echo=echo)

        # Создание асинхронных сессии
        self.__session_factory = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
            autoflush=False,
        )

    async def session_dependency(self) -> AsyncSession:
        """
        Метод для открытия асинхронной сессии
        :return: AsyncSession
        """
        async with self.__session_factory() as session:
            yield session
            await session.close()


db_helper = DatabaseHelper(
    url=settings.DATABASE_URL_asyncpg,
    echo=settings.DB_ECHO,
)
