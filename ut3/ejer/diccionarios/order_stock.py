# ***********
# ¿HAY STOCK?
# ***********


def run(stock: dict, merch: str, amount: int) -> bool:
    available = False
    for obj, loot in stock.items():
        if obj == merch and loot >= amount:
            available = True

    return available


if __name__ == '__main__':
    run({'pen': 20, 'cup': 11, 'keyring': 40}, 'cup', 9)
