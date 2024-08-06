class HabitValidator:
    """Валидатор привычки"""

    def __init__(self, related_habit: str, award: str, pleasant_habit: str):
        self.related_habit = related_habit
        self.award = award
        self.pleasant_habit = pleasant_habit

    def __call__(self, value: dict, related_habit_instance: dict | None = None):
        related_habit = dict(value).get(self.related_habit)  # связанная привычка
        pleasant_habit = dict(value).get(
            self.pleasant_habit
        )  # признак приятной привычки
        award = dict(value).get(self.award)  # вознаграждение

        if related_habit and award:
            return "Нельзя выбрать одновременно вознаграждение и связаную приятную привычку"
        related_habit_instance = (
            related_habit_instance.get(self.pleasant_habit)
            if related_habit_instance
            else None
        )

        if not related_habit_instance:
            if related_habit and not related_habit_instance:
                return "вы выбрали не приятную привычу"

        if pleasant_habit and award:
            return "У приятной привычки не может быть вознаграждения"

        if not pleasant_habit and not award and not related_habit:
            return "У привычки должно быть вознаграждение либо связанная привычка"


# habit_data = {
#     "place": "home",
#     "time_start": "09:00",
#     "action": "exercise",
#     "pleasant_habit": True,
#     "related_habit": 1,
#     "frequency": 1,
#     "award": None,
#     "time_to_complete": 60,
#     "is_published": False,
# }
#
# habit_data_2 = {
#     "place": "home",
#     "time_start": "09:00",
#     "action": "exercise",
#     "pleasant_habit": False,
#     "related_habit": None,
#     "frequency": 1,
#     "award": "energy drink",
#     "time_to_complete": 60,
#     "is_published": False,
# }
# habit_orm_instance = HabitOrm(**habit_data)  # create an instance of HabitOrm
# validator = HabitValidator("related_habit", "award", "pleasant_habit").__call__(
#     habit_data, habit_data_2
# )
# validator(habit_data)
