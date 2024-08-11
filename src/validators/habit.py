from src.repositories.models.habit import HabitOrm
from src.schemas.habit import HabitCreate


class HabitValidator:

    async def __call__(
        self, habit_create: HabitCreate, relation_habit: HabitOrm | None, user: int
    ):
        # Проверка на одновременное заполнение reward и related_habit
        if (habit_create.award is not None) and (
            habit_create.related_habit is not None
        ):
            raise ValueError(
                "Нельзя указывать одновременно вознаграждение и связанную привычку."
            )
        if (habit_create.pleasant_habit is True) and (
            habit_create.related_habit is not None
        ):
            raise ValueError(
                "Нельзя указывать одновременно что это привычка приятная и связанную привычку"
            )
        # Проверка на одновременное заполнение связканной привычки и вознаграждение
        if (habit_create.pleasant_habit is True) and (habit_create.award is not None):
            raise ValueError(
                "Нельзя указывать одновременно что это приятная привычка и вознаграждение"
            )
        # Проверка связанной привычки
        if (habit_create.related_habit is not None) and (relation_habit is not None):
            if not relation_habit.pleasant_habit:
                raise ValueError("Связанная привычка должна быть приятной.")
            if relation_habit.user_id != user:
                raise ValueError(
                    "Связанная привычка должна принадлежать тому же пользователю."
                )
