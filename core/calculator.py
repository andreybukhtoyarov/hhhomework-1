from core.decorators import cache_decorator


@cache_decorator
def calculator(a: float, b: float, operation: str) -> float:
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    math_funk = {'+': lambda a, b: a + b,
                 '-': lambda a, b: a - b,
                 '/': lambda a, b: a / b,
                 '*': lambda a, b: a * b,
                 '**': lambda a, b: a ** b}
    op = math_funk.get(operation, lambda a, b: 'Вы ввели не подерживаемую операцию')
    return op(a, b)


if __name__ == '__main__':
    # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
    try:
        a = float(input('Введите число: '))
        b = float(input('Введите число: '))
        operation = input('Введите операцию: ')
        print('Результат: ', calculator(a, b, operation))
    except ValueError as err:
        print(err, 'Вы ввели не число')
