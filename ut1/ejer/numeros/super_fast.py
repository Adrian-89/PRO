# **********************
# ANIMALES SUPER RÁPIDOS
# **********************


def run(speed_km_h: float) -> float:
    speed_cm_s = int(speed_km_h * 27.777777777778)

    return speed_cm_s


if __name__ == '__main__':
    run(1.08)
