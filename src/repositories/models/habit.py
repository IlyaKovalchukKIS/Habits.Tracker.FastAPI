import enum
from datetime import datetime

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.repositories.db_helper import Base, str_40
from src.repositories.models.user import UserOrm


class Frequency(enum.Enum):
    DAILY_ONE = "DAILY_ONE"  # 1 раз в день
    DAILY_TWO = "DAILY_TWO"  # 1 раз в 2 дня
    DAILY_THREE = "DAILY_THREE"  # 1 раз в 3 дня
    DAILY_FOUR = "DAILY_FOUR"  # 1 раз в 4 дня
    DAILY_FIVE = "DAILY_FIVE"  # 1 раз в 5 дней
    DAILY_SIX = "DAILY_SIX"  # 1 раз в 6 дней
    DAILY_SEVEN = "DAILY_SEVEN"  # 1 раз в 7 дней


class HabitOrm(Base):
    __tablename__ = "habits"

    id: Mapped[int] = mapped_column(primary_key=True)

    place: Mapped[str_40]  # место выполнения привычки

    time_start: Mapped[datetime | None] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )  # время начала выполнения привычки

    action: Mapped[str_40]  # действие привычки

    pleasant_habit: Mapped[bool | None] = mapped_column(
        nullable=True, default=False
    )  # признак приятной привычки

    related_habit: Mapped[int | None] = mapped_column(
        ForeignKey("habits.id"), nullable=True
    )  # связанная привычка

    frequency: Mapped[Frequency] = mapped_column(
        default=Frequency.DAILY_ONE
    )  # частота выполнения

    award: Mapped[str_40 | None]  # награда

    time_to_complete: Mapped[int | None] = mapped_column(
        default=120
    )  # время на выполнение

    is_published: Mapped[bool | None] = mapped_column(
        default=False
    )  # публикация привычки

    last_send: Mapped[datetime | None] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )  # время последнего выполнения привычки

    created_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )  # время создания привычки

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE")
    )  # id пользователя

    user: Mapped[UserOrm] = relationship(
        "UserOrm", back_populates="habits"
    )  # связь с таблицей Users
