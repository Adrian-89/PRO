# *********************
# ENCONTRANDO ISOGRAMAS
# *********************


def run(text: str) -> bool:
    ALPHABET = ("abcdefghijklmnñopqrstuvwxyz")
    alphanum = []
    is_isogram = True
    
    for word in text.lower:
        if word in ALPHABET:
            if word not in alphanum:
                alphanum.append(word)

        else:
            is_isogram = False
            break
    return is_isogram


if __name__ == '__main__':
    run('lumberjacks')
