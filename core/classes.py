class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    car_model = ''
    car_mark = ''

    def __init__(self, car_model: str, car_mark: str) -> None:
        self.car_model = car_model
        self.car_mark = car_mark

    def __repr__(self) -> str:
        return '{} - {}'.format(self.car_mark, self.car_model)

    pass


class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    cars = []

    def __init__(self, cars: list) -> None:
        self.cars = cars

    def __len__(self) -> int:
        return len(self.cars)

    def __getitem__(self, index) -> Car:
        return self.cars[index]

    def __add__(self, other: Car) -> None:
        self.cars.append(other)

    def __delete__(self, index: int) -> Car:
        return self.cars.pop(index)

    pass
