# ******************
# DESCOMPONIENDO RGB
# ******************


def run(rgb_color: str) -> tuple:
    particionado = rgb_color.partition('')
    striping = str(particionado).strip(2)

    red_index = rgb_color[1:4]
    green_index = rgb_color
    strping = rgb_color.rstrip(red_index)
    r_side = rgb_color.strip(")'")
    clean_rgb = r_side.strip(',')

    red = green = blue = rgb_color.partition('')

    return red, green, blue


if __name__ == '__main__':
    run('(161,49,247)')
