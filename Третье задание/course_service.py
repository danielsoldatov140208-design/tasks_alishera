class Course:
    def __init__(self, title: str, capacity: int):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Название курса не может быть пустым.")
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Количество мест должно быть положительным целым числом.")

        self.title = title.strip()
        self.capacity = capacity
        self.enrolled = 0

    def available_places(self) -> int:
        return self.capacity - self.enrolled

    def enroll(self) -> int:
        if self.is_full:
            raise ValueError("Нет свободных мест на курсе.")
        self.enrolled += 1
        return self.available_places()

    def cancel_enrollment(self) -> int:
        if self.enrolled <= 0:
            raise ValueError("Нет зарегистрированных студентов для отмены.")
        self.enrolled -= 1
        return self.available_places()

    @property
    def is_full(self) -> bool:
        return self.enrolled >= self.capacity


class IntensiveCourse(Course):
    def __init__(self, title: str, capacity: int, hours_per_week: int):
        super().__init__(title, capacity)
        if not isinstance(hours_per_week, int) or not (6 <= hours_per_week <= 20):
            raise ValueError("Часы в неделю должны быть целым числом от 6 до 20.")
        self.hours_per_week = hours_per_week

    def workload_level(self) -> str:
        if 6 <= self.hours_per_week <= 10:
            return "средняя"
        return "высокая"