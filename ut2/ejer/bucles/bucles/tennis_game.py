# *****************
# UN JUEGO AL TENIS
# *****************


def run(points: str) -> str:
    a_winner = 0
    b_winner = 0
    for best in points:
        if best == 'A':
            a_winner += 1
        elif best == 'B':
            b_winner += 1
    
    if a_winner > b_winner:
        winner = 'A'
    else:
        winner = 'B'
    

    return winner


if __name__ == '__main__':
    run('ABAABA')