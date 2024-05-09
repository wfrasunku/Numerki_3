import mathLib


def caluclate_nodes(functions: list, left_boundary: float, right_boundary: float) -> float:
    a = mathLib.evaluate_composite(left_boundary, functions)
    h = mathLib.evaluate_composite((left_boundary + right_boundary) / 2, functions)
    b = mathLib.evaluate_composite(right_boundary, functions)

    result = ((a + 4 * h + b) * (right_boundary - left_boundary))/6
    return result


def newton_cotes(functions: list, left_boundary: float, right_boundary: float, precision: float) -> (float, int):
    previous = 0
    n = 1
    while True:
        current = 0
        delta = (right_boundary - left_boundary) / n
        a = left_boundary
        b = left_boundary + delta
        while b <= right_boundary:
            temp = caluclate_nodes(functions, a, b)
            current += temp
            a += delta
            b += delta
        n += 1
        if abs(current - previous) <= precision:
            return current, n - 1
        previous = current

