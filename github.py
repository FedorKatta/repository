from typing import Union


def kalculator():
    """Простой калькулятор"""

    problem = input().split()

    number1, sign, number2 = float(problem[0]), problem[1], float(problem[2])

    match sign:
        case "+": answer = summary(number1, number2)
        case "-": answer = subtract(number1, number2)
        case "*": answer = multiplication(number1, number2)
        case "/": answer = division(number1, number2)
        case _: answer = "Неизвестный знак"

    print(answer)


def summary(a: float, b: float) -> Union[int, float]:
    return a + b


def subtract(a: float, b: float) -> Union[int, float]:
    return a - b


def multiplication(a: float, b: float) -> Union[int, float]:
    return round(a * b, 10)


def division(a: float, b: float) -> Union[int, float, str]:
    if b == 0:
        return "Деление запрещено"
    return round(a / b, 10)


if __name__ == "__main__":
    while True:
        kalculator()
