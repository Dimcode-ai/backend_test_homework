import math

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    return math.sqrt(Number)


def calc(your_number):
    """Мы вычисляем квадратный корень."""
    if your_number <= 0:
        return
    calculate = CalculateSquareRoot(your_number)
    print(
        f'Мы вычислили квадратный корень'
        f' из введённого вами числа. '
        f'Это будет: {calculate}')


print(message)
calc(25.5)
