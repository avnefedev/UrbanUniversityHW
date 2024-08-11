# Словари
my_dict = {'Mary': 1997, 'Max': 2000, 'Bob': 1990, 'Sam': 1980}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Mary', 'Нет такого ключа'))
print('Not existing value:', my_dict.get('mary', 'Нет такого ключа'))
my_dict.update({'Rob': 2003, 'Kevin': 1978})
print('Deleted value:', my_dict.pop('Max'))
print('Modified dict:', my_dict)

# Множества
my_set = {1, 2, 3, 1, True, True, 'Car', 'Car'} # True питон приравнивает к 1
print('Set:', my_set)
my_set.add(7)
my_set.add(8)
my_set.discard(True) # удалит 1
print('Modified set:', my_set)
