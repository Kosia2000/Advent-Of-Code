filename = "text.txt"


def open_file():
    with open(filename, "r") as file:
        data = file.readlines()
        lines = [line.strip() for line in data]
    return lines


def _get_row(line):
    left = 0
    right = 127
    half = (right+1)/2

    for seat in range(0, 7):
        if line[seat] == "F":
            right -= half
        else:
            left += half
        half = half // 2
    return left


def _get_col(line):
    left = 0
    right = 7
    half = (right+1)/2

    for seat in range(7, 10):
        if line[seat] == "L":
            right -= half
        else:
            left += half
        half /= 2
    return left


def max_number():
    seats_ID = []
    number = 0
    count = 0
    lines = open_file()
    for line in lines:
        answer = (_get_row(line) * 8) + _get_col(line)
        count+=1
        seats_ID.append(answer)

        if answer > number:
            number = answer

    seats_ID.sort()

    stop_flag = True
    seats_ID
    for seat in seats_ID:
        seat = int(seat)
        if stop_flag:
            if seats_ID[seat]+1 != seats_ID[seat+1]:
                print("Missing seat: {}".format(seats_ID[seat]+1))
                stop_flag = False

    print("Max seat number: {}".format(number))


max_number()
