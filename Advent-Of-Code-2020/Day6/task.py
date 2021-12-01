filename = "text.txt"


def open_file():
    with open(filename, "r") as file:
        data = file.readlines()
        lines = [line.strip() for line in data]
    return lines


def _get_ans(response):
    questions = []
    for c in response:
        if c not in questions:
            questions.append(c)
    length = len(questions)
    return length


def _get_all(response):
    questions = []
    flag = True

    for c in response[0]:
        flag = True
        for line in response:
            if c not in line:
                flag = False
        if flag and (c not in questions):
            questions.append(c)

    lenght = len(questions)
    return lenght


def count_sum():
    lines = open_file()
    sum1 = 0
    sum2 = 0
    resp1 = ''
    resp2 = []
    for line in lines:
        if line != '':
            resp1 += line
            resp2.append(line)
        else:
            sum1 += _get_ans(resp1)
            sum2 += _get_all(resp2)
            resp1 = ''
            resp2 = []
    sum1 += _get_ans(resp1)
    sum2 += _get_all(resp2)

    print("Part one: {}".format(sum1))
    print("Part two: {}".format(sum2))


count_sum()
