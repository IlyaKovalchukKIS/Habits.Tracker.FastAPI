from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.repositories.db_helper import Base


class UserOrm(SQLAlchemyBaseUserTable[int], Base):
    """
        id: номер пользователя
        email: почта пользователя
        name_telegram: имя пользователя
        id_telegram: id пользователя в телеграм
        hashed_password: хэш пароля
        created_at: дата создания пользователя
        is_active: активен ли пользователь
        is_superuser: является ли пользователь суперпользователем
        is_verified: подтвержден ли пользователь
        habits: список привычек пользователя
        """
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    name_telegram: Mapped[str]
    id_telegram: Mapped[int] = mapped_column(unique=True, index=True, nullable=True)
    hashed_password: str
    created_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )
    is_active: bool
    is_superuser: bool
    is_verified: bool

    habits = relationship("HabitOrm", back_populates="user")
