data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

'''Первый способ'''

# data_structure = [1, 2, 3]
# data_structure = {'a': 4, 'b': 5}

# def defenition_type(val):
#     if isinstance(val, (int, float)):
#         return val
#     elif isinstance(val, str):
#         return len(val)
#     elif isinstance(val, (tuple, set)):
#         val_list = list(val)
#         return sum_list(*val_list)
#     elif isinstance(val, list):
#         return sum_list(*val)
#     elif isinstance(val, dict):
#         return sum_dict(val)
#
# def sum_list(*args):
#     a = 0
#     for i in args:
#         a += defenition_type(i)
#     return a
#
# def sum_dict(value: dict):
#     a = 0
#     for key in value.keys():
#         a += defenition_type(key)
#     for value in value.values():
#         a += defenition_type(value)
#     return a

# def calculate_structure_sum(value):
#     answer = 0
#     for i in value:
#         answer += defenition_type(i)
#     return answer

'''Второй способ'''
def calculate_structure_sum(value):
    result = 0
    if isinstance(value, (int, float)):
        result += value
    elif isinstance(value, str):
        result += len(value)
    elif isinstance(value, dict):
        for key in value.keys():
            result += calculate_structure_sum(key)
        for value in value.values():
            result += calculate_structure_sum(value)
    else:
        for val in value:
            if isinstance(val, (int, float)):
                result += val
            elif isinstance(val, str):
                result += len(val)
            elif isinstance(val, (tuple, set)):
                val_list = list(val)
                for i in val_list:
                    result += calculate_structure_sum(i)
            elif isinstance(val, list):
                for i in val:
                    result += calculate_structure_sum(i)
            elif isinstance(val, dict):
                for key in val.keys():
                    result += calculate_structure_sum(key)
                for value in val.values():
                    result += calculate_structure_sum(value)
    return result

result = calculate_structure_sum(data_structure)
print(result)
