def is_prime(func):
    def wrapper(*args):
        original_func = func(*args)
        for i in range(2, int(original_func ** 0.5) + 1):
            if original_func % i == 0:
                return f'Не простое число: {original_func}'
        return f'простое число: {original_func}'
    return wrapper


@is_prime
def sum_three(*args):
    res = sum(args)
    return res


result = sum_three(3, 3, 6, 7)
print(result)
