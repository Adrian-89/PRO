def func(x):
    return x**2


def calc_rect_area(width, heigth):
    return width * heigth


def frange(start, end, step):
    result = []
    current = start

    while current <= end:
        result.append(current)
        current += step

    return result


def integrate(start, end, step):
    area_rect = 0.0
    inter = frange(start, end, step)
    area_rect = 0
    for i in inter:
        yaxis = func(i)
        area_rect += calc_rect_area(step, yaxis)

    return area_rect


if __name__ == "__main__":

    print(integrate(0, 2, 0.01))
