# ******************
# LA PALABRA PERDIDA
# ******************


def run(text: str, target_word: str, replace_word: str) -> str:
    phrase = text.find(target_word)
    first_zone = text[:phrase]
    second_zone = text[phrase + len(target_word) :]
    mtext = first_zone + replace_word + second_zone

    return mtext


if __name__ == '__main__':
    run('This is a beautiful night on the Atlantic', 'beautiful', 'terrible')
