import mathLib


def simpson_method(functions: list, left_boundary: float, right_boundary: float) -> float:
    a = mathLib.evaluate_composite(left_boundary, functions)
    h = mathLib.evaluate_composite((left_boundary + right_boundary) / 2, functions)
    b = mathLib.evaluate_composite(right_boundary, functions)

    result = ((a + 4 * h + b) * (right_boundary - left_boundary))/6
    return result


def newton_cotes(functions: list, left_boundary: float, right_boundary: float, precision: float) -> float:
    previous = 0
    n = 1
    while True:
        current = 0
        delta = (right_boundary - left_boundary) / n
        a = left_boundary
        b = left_boundary + delta
        while b <= right_boundary:
            temp = simpson_method(functions, a, b)
            current += temp
            a += delta
            b += delta
        n += 1
        if abs(current - previous) <= abs(precision):
            return current
        previous = current


def newton_cotes_limes(functions: list, precision: float) -> float:
    a = result = 0
    b = 0.5
    while True:
        current = newton_cotes(functions, a, b, precision)
        result += current
        if abs(current) <= abs(precision):
            return result
        a = b
        b += (1 - b)/2
