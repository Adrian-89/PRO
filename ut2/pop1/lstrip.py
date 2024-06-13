# **********
# LEFT STRIP
# **********


def run(text: str, blacklist: str) -> str:
    strip = text[-7:]
    blacklist = text[:-7]

    if blacklist:
        strip

    words = strip

    stext = words

    return stext


if __name__ == '__main__':
    run('955428PAYLOAD', '0123456789')
