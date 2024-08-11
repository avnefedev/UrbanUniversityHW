def print_params(a = 1, b = 'Строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, 'name', False]
values_dict = {'a': 'bob', 'b': 4, 'c': [1, 2, 3]}

print_params(*values_list)
print_params(**values_dict)

values_list2 = [1, 'fast']

print_params(*values_list2)
