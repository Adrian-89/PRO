# ***********************************
# POR ENCIMA Y POR DEBAJO DE LA MEDIA
# ***********************************


def run(marks: list) -> tuple:
    below_marks = []
    above_marks = []
    marks_operation = sum(marks)
    marks_average = marks_operation / len(marks)

    for items in marks:
        if items <= marks_average:
            below_marks.append(items)
        elif items > marks_average:
            above_marks.append(items)

    below_avg = below_marks
    above_avg = above_marks

    return below_avg, above_avg


if __name__ == '__main__':
    run([3.7, 1.2, 9.5, 4.7, 6.3, 7.2, 3.8, 1.1, 1.4])
