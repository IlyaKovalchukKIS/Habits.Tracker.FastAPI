from datetime import datetime
from pydantic import BaseModel
from src.repositories import str_40, Frequency


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
    time_start: datetime
    action: str_40
    pleasant_habit: bool | None
    related_habit: int | None
    frequency: Frequency
    award: str_40 | None
    time_to_complete: int | 120
    is_published: bool | None


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
    last_send: datetime

    class Config:
        orm_mode = True


class HabitUpdate(HabitBase):
    pass
