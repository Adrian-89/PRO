# *******************
# SEPARANDO EL TIEMPO
# *******************


def run(seconds: int) -> tuple:
    calc_hours = seconds // 3600
    calc_minutes = seconds // 60 - calc_hours * 60
    calc_seconds = seconds % 60
    hours = calc_hours
    minutes = calc_minutes
    seconds = calc_seconds

    return hours, minutes, seconds


if __name__ == '__main__':
    run(31256)
