class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float
                 ) -> str:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories
    def get_message(self):
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.distance} ч.; '
                f'Дистанция: {self.distance} км; '
                f'Ср. корость: {self.speed} км/ч; '
                f'Потрачено ккал: {self.calories}.'
        )


M_IN_KM = 1000
MINUTES_IN_HOUR = 60
SM_IN_M = 100

class Training:
    """Базовый класс тренировки."""
    LEN_STEP = None

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed = Training.get_distance() / self.duration
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage.get_message()


class Running(Training):
    """Тренировка: бег."""
    LEN_STEP = 0.65

    def get_spent_calories(self) -> float:
        CALORIES_MEAN_SPEED_MULTIPLIER = 18
        CALORIES_MEAN_SPEED_SHIFT = 1.79
        calories = ((CALORIES_MEAN_SPEED_MULTIPLIER * Running.get_mean_speed() + 
                    CALORIES_MEAN_SPEED_SHIFT) * self.weight / M_IN_KM * 
                    self.duration / MINUTES_IN_HOUR)
        return calories            

class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: int
                 ) -> None:
        super().__init__(action)
        super().__init__(duration)
        super().__init__(weight)
        self.height = height

    def get_spent_calories(self) -> float:
        WEIGHT_MULTIPLIER_FIRST = 0.035
        WEIGHT_MULTIPLIER_SECOND = 0.029
        calories = ((WEIGHT_MULTIPLIER_FIRST * self.weight +
                    (SportsWalking.get_mean_speed() ** 2 / self.height / SM_IN_M) *
                    WEIGHT_MULTIPLIER_SECOND * self.weight) *
                    self.duration / MINUTES_IN_HOUR)

class Swimming(Training):
    """Тренировка: плавание."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 lenght_pool: float,
                 count_pool: int
                 ) -> None:
        super().__init__(action)
        super().__init__(duration)
        super().__init__(weight)
        self.lenght_pool = lenght_pool
        self.count_pool = count_pool
    


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

