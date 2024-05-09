import mathLib


def caluclate_nodes(functions: list, left_boundary: float, right_boundary: float) -> (float, float):
    a = mathLib.evaluate_composite(left_boundary, functions)
    h = mathLib.evaluate_composite((left_boundary + right_boundary) / 2, functions)
    b = mathLib.evaluate_composite(right_boundary, functions)

    return a + b, h


def newton_cotes(functions: list, left_boundary: float, right_boundary: float, precision: float) -> (float, int):
    current = 40
    previous = 0
    n = 1
    while not abs(current - previous) <= precision:
        delta = (right_boundary - left_boundary) / n
        a = left_boundary
        b = left_boundary + delta
        tempX = tempH = 0
        while b <= right_boundary:
            x, h = caluclate_nodes(functions, a, b)
            tempX += x
            tempH += h
            a += delta
            b += delta
        current = ((tempX + 4 * tempH) * (b - a))/6
        n += 1
        previous = current

    return current, n - 1