data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def validator(val):
    if isinstance(val, int) or isinstance(val, float):
        return val
    elif isinstance(val, str):
        return len(val)
    elif isinstance(val, tuple) or isinstance(val, set):
        val_list = list(val)
        return sum_list(*val_list)
    elif isinstance(val, list):
        return sum_list(*val)
    elif isinstance(val, dict):
        return sum_dict(val)

def sum_list(*args):
    a = 0
    for i in args:
        a += validator(i)
    return a

def sum_dict(value: dict):
    a = 0
    for key in value.keys():
        a += validator(key)
    for value in value.values():
        a += validator(value)
    return a

def calculate_structure_sum(value):
    answer = 0
    for i in value:
        answer += validator(i)
    return answer

result = calculate_structure_sum(data_structure)
print(result)
