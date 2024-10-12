def is_prime(func):
    def wrapper(*args):
        count = 0
        sum1 = func(*args)
        for i in range(1, sum1 + 1):
            if sum1 % i == 0:
                count += 1
        if count == 2:
            return f'Простое\n{sum1}'
        else:
            return f'Составное\n{sum1}'
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(3, 2, 6)
print(result)
