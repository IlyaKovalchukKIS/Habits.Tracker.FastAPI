import datetime
from typing import List

from pydantic import BaseModel, conint
from src.repositories.db_helper import str_40
from src.repositories.models.habit import Frequency


class HabitBase(BaseModel):
    """
    place: место выполнения привычки
    time_start: время начала выполнения привычки
    action: действие привычки
    pleasant_habit: признак приятной привычки
    related_habit: связанная привычка
    frequency: частота выполнения
    award: награда
    time_to_complete: время на выполнение
    is_published: публикация привычки
    """

    place: str_40
    time_start: datetime.datetime | None = None
    action: str_40
    pleasant_habit: bool | None = False
    related_habit: int | None | List["HabitRead"] = None
    frequency: Frequency
    award: str_40 | None = None
    time_to_complete: conint(ge=0, le=120) = 120
    is_published: bool | None = False


class HabitCreate(HabitBase):
    pass


class HabitRead(HabitBase):
    """
    id: номер привычки
    user_id: id пользователя
    last_send: время последнего выполнения привычки
    """

    id: int
    user_id: int
    last_send: datetime.datetime

    class Config:
        from_attributes = True


class HabitUpdate(HabitBase):
    pass
