from datetime import datetime
from typing import Optional, Annotated

from sqlalchemy import Boolean, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship, mapped_column, Mapped, DeclarativeBase
import enum

str_40 = Annotated[str, mapped_column(String(40))]


class Frequency(enum.Enum):
    DAILY_ONE = 1  # 1 раз в день
    DAILY_TWO = 2  # 1 раз в 2 дня
    DAILY_THREE = 3  # 1 раз в 3 дня
    DAILY_FOUR = 4  # 1 раз в 4 дня
    DAILY_FIVE = 5  # 1 раз в 5 дней
    DAILY_SIX = 6  # 1 раз в 6 дней
    DAILY_SEVEN = 7  # 1 раз в 7 дней


class Base(DeclarativeBase):
    pass


class UserOrm(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    id_telegram: Mapped[int] = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)

    habits = relationship("HabitOrm", back_populates="user")


class HabitOrm(Base):
    __tablename__ = "habits"

    id: Mapped[int] = mapped_column(primary_key=True)
    place: Mapped[str]  # место выполнения привычки
    time: Mapped[datetime]  # время начала выполнения привычки
    action: Mapped[str]  # действие привычки
    pleasant_habit: Mapped[bool | None] = mapped_column(
        nullable=True, default=False
    )  # признак приятной привычки
    related_habit: Mapped[int | None] = mapped_column(
        ForeignKey("habits.id"), nullable=True
    )  # связанная привычка
    frequency: Mapped[Frequency] = mapped_column(
        default=Frequency.DAILY_ONE
    )  # частота выполнения
    award: Mapped[str | None]  # награда
    time_to_complete: Mapped[int | None] = mapped_column(
        default=120
    )  # время на выполнение
    is_published: Mapped[bool | None] = mapped_column(
        default=False
    )  # публикация привычки
    last_send: Mapped[datetime | None]  # время последнего выполнения привычки
    created_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )  # время создания привычки
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE")
    )  # id пользователя

    user: Mapped[UserOrm] = relationship(
        "UserOrm", back_populates="habits"
    )  # связь с таблицей Users
