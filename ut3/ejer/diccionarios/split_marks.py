# *********************
# CADA NOTA EN SU SITIO
# *********************


def run(marks: dict) -> tuple:
    marks_notes = {k.lower(): v for k, v in marks.items() if v < 5}
    marks_notes2 = {k.upper(): v for k, v in marks.items() if v >= 5}
    passed = marks_notes2
    failed = marks_notes
    return passed, failed


if __name__ == '__main__':
    run({'Ana': 4, 'Domingo': 7, 'Eva': 5, 'Álvaro': 3, 'Juan': 8, 'Belén': 1})
