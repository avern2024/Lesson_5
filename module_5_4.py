class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        name = args[0]  # Получаем название из первого аргумента
        cls.houses_history.append(name)  # Добавляем название в историю домов
        return super(House, cls).__new__(cls)  # Создаем новый экземпляр

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            print("\n".join(str(i) for i in range(1, new_floor + 1)))
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return isinstance(other, House) and self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return isinstance(other, House) and self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        return isinstance(other, House) and self.number_of_floors > other.number_of_floors

    def __le__(self, other):
        return isinstance(other, House) and self.number_of_floors <= other.number_of_floors

    def __ge__(self, other):
        return isinstance(other, House) and self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return isinstance(other, House) and self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        if isinstance(other, House):
            return House(f"{self.name} + {other.name}", self.number_of_floors + other.number_of_floors)
        elif isinstance(other, int):
            return House(self.name, self.number_of_floors + other)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, House):
            self.number_of_floors += other.number_of_floors
        elif isinstance(other, int):
            self.number_of_floors += other
        return self

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


# Пример использования
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
