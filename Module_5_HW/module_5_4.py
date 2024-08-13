class House:
    houses_history =[]
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floors = number_of_floor

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor+1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, (int, House)):
            return bool(self.number_of_floors == other)
        else:
            return f'other - не число'

    def __lt__(self, other):
        if isinstance(other, (int, House)):
            return self.number_of_floors < other
        else:
            return f'other - не число'

    def __le__(self, other):
        if isinstance(other, (int, House)):
            return self.number_of_floors <= other
        else:
            return f'other - не число'

    def __gt__(self, other):
        if isinstance(other, (int, House)):
            return self.number_of_floors > other
        else:
            return f'other - не число'

    def __ge__(self, other):
        if isinstance(other, (int, House)):
            return self.number_of_floors >= other
        else:
            return f'other - не число'

    def __ne__(self, other):
        if isinstance(other, (int, House)):
            return self.number_of_floors != other
        else:
            return f'other - не число'

    def __add__(self, other):
        if isinstance(other, (int, House)):
            return House(self.name, self.number_of_floors + other)
        else:
            return f'other - не число'

    def __radd__(self, other):
        # if isinstance(other, (int, House)):
        #     return House(self.name, self.number_of_floors + other)
        # else:
        #     return f'other - не число'
        return self + other

    def __iadd__(self, other):
        # if isinstance(other, int):
        #     return House(self.name, self.number_of_floors + other)
        # else:
        #     return f'other - не число'
        return self + other

    def __del__(self):
        print(f'{self.name} снесен, но он навсегда останется в нашей памяти')


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

