from datetime import datetime

from pydantic import EmailStr
from sqlalchemy import text
from sqlalchemy.orm import relationship, mapped_column, Mapped

from src.repositories import Base, str_40, HabitModels


class UserOrm(Base):
    """
    id: номер пользователя
    email: почта пользователя
    name_telegram: имя пользователя
    id_telegram: id пользователя в телеграм
    hashed_password: хэш пароля
    created_at: дата создания пользователя
    is_active: активен ли пользователь
    is_superuser: является ли пользователь суперпользователем
    is_admin: является ли пользователь админом
    habits: список привычек пользователя
    """

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[EmailStr] = mapped_column(unique=True, index=True)
    id_telegram: Mapped[int] = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str_40]
    created_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    is_admin: Mapped[bool] = mapped_column(default=False)

    habits = relationship("HabitOrm", back_populates="user")
