immutable_var = (1, True, 'String', 1.3, [1, 2, 3])
print(immutable_var)
# immutable_var[0] = 100 программа выдаст ошибку, так как нельзя менять неизменяемые значения в кортеже.
immutable_var[4][0] = 100 # программа продолжит работу так как мы меняем изменяемое значение внутри кортежа
print(immutable_var)

mutable_list = [1, True, 'String', 1.3, [1, 2, 3]]
mutable_list[0] = 200
mutable_list.append(123)
mutable_list.extend('HELLO')
print(mutable_list)
