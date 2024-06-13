# ****************
# YELLOW SUBMARINE
# ****************
from pathlib import Path


def run(route_path: Path) -> tuple:
    MIN_DEPTH = 0
    MAX_DEPTH = 600
    DISTANCE_CONSUMPTION_RATE = 3
    DEPTH_CONSUMPTION_RATE = 2

    f = open(route_path)
    distance = 0
    depth = 0
    fuel = int(f.readline().strip())
    moves = []
    moves = [[int(h) for h in v.split(':')] for v in f.readline().strip().split(',')]
    for x, y in moves:
        distance += x
        depth += y
        fuel -= abs(x) * DISTANCE_CONSUMPTION_RATE + abs(y) * DEPTH_CONSUMPTION_RATE
        if depth < MIN_DEPTH:
            break
        if depth > MAX_DEPTH:
            break
        if fuel <= 0:
            break

    return distance, depth, fuel


if __name__ == '__main__':
    run('data/submarine/route1.dat')
