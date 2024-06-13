# ***************
# UN SET AL TENIS
# ***************


def run(points: str) -> tuple:
    POINTS_TO_SET = 4
    a_points = 0
    b_points = 0
    tie_break_a = 0
    tie_break_b = 0
    a_sets = 0
    b_sets = 0
    for best in points:
        if best == 'A':
            a_points += 1
        elif best == 'B':
            b_points += 1
        if a_points >= POINTS_TO_SET and a_points - b_points >= 2:
            a_sets += 1
            a_points = 0
            b_points = 0
        elif b_points >= POINTS_TO_SET and b_points - a_points >= 2:
            b_sets += 1
            b_points = 0
            a_points = 0
        if a_sets == 6 and b_sets == 6 :
            a_points = 0
            b_points = 0 
            if best == 'A':
                tie_break_a += 1
            elif best == 'B':
                tie_break_b += 1
            if tie_break_a >= 7 and tie_break_a - tie_break_b >= 2:
                a_sets += 1
                tie_break_a = 0
                tie_break_b = 0
            elif tie_break_b >= 7 and tie_break_b - tie_break_a >= 2:
                b_sets += 1
                tie_break_a = 0
                tie_break_b = 0

    games_player1 = a_sets
    games_player2 = b_sets

    return games_player1, games_player2


if __name__ == '__main__':
    run('AABBAABABBBABABABBBAAABBBABAABBABBAABBBABABBAAAABBBBABBBAB')
