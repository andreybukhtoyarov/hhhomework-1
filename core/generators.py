from random import randint


# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
def gen(n: int) -> int:
    for i in range(n):
        yield randint(1, 101)


# написать генераторное выражение, которое делает то же самое
gen = (randint(1, 101) for i in range(10))
