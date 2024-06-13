# ********************
# DESCIFRANDO CIUDADES
# ********************


def run(cinfo: str) -> dict:
    splited_info = cinfo.split(';')
    cities = {}
    for keys in splited_info:
        city, population = keys.split(':')
        cities[city] = int(population)

    return cities


if __name__ == '__main__':
    run('Tokyo:38_140_000;Delhi:26_454_000;Shanghai:24_484_000;Mumbai:21_357_000')
