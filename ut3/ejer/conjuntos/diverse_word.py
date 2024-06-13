# ***************
# PALABRA DIVERSA
# ***************


def run(words: list) -> str:
    dword = ""
    most_different = False
    for item in words:
        items_diff = len(set(item))

        if items_diff > most_different:
            most_different = items_diff
            dword = item
    return dword


if __name__ == '__main__':
    run(['dictionary', 'turtle', 'flexibility', 'humanity'])
