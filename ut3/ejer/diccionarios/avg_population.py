# ******************
# POBLACIÓN PROMEDIO
# ******************


def run(pdata: dict) -> dict:
    avg_data = pdata.copy()
    total = sum(pdata.values())
    for population in pdata:
        pdata[population] = round((pdata[population]) / total * 100, 3)

    avg_data = pdata
    return avg_data


if __name__ == '__main__':
    run({'Tokyo': 38140000, 'Delhi': 26454000, 'Shanghai': 24484000, 'Mumbai': 21357000})
