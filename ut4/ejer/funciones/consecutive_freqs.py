# ************************************
# FRECUENCIA DE ELEMENTOS CONSECUTIVOS
# ************************************


def cfreq2(items, /, as_string=False):
    result = []
    if items:
        current_value = items[0]
        freq = 1
        for item in items[1:]:
            if item != current_value:
                result.append((current_value, freq))
                freq = 1
                current_value = item
            else:
                freq += 1
        result.append((current_value, freq))
        return result


def cfreq(items, /, as_string=False):
    result = cfreq2(items)
    if as_string:
        str_output = []
        for num, freq in result:
            str_output.append(f"{num}:{freq}")
        result = ",".join([f"{num}:{freq}" for num, freq in result])
    return result