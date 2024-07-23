def key_for_req(n):
    # n = int(input('Введите значение: '))
    all_key = ''
    def check_answer(a, b):
        if n % (a + b) == 0:
            return True

    for i in range(1, n):
        for j in range(i + 1, n):
            flag = check_answer(i, j)
            if flag:
                all_key += str(i)
                all_key += str(j)

    print(f'Для числа {n} ответ - {all_key}')

for i in range(3, 21): # Проверка ключей для всех значений
    key_for_req(i)
