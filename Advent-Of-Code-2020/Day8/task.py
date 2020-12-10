filename = 'text.txt'


def open_file():
    lines = []
    with open(filename, "r") as file:
        data = file.readlines()
        lines = [line.strip().split() for line in data]

    return lines


def check(lines):

    accumulator = 0
    i = 0

    used_commands = []
    flag = True
    flag2 = True

    while flag and i < len(lines):

        code = lines[i][0]
        number = int(lines[i][1])

        if i not in used_commands:

            if code == "acc":
                accumulator += number
                used_commands.append(i)

                i += 1

            elif code == "jmp":
                used_commands.append(i)

                i += number

            else:
                used_commands.append(i)
                i += 1

        else:
            flag = False

    if flag:
        print("Accumulator task2: {}".format(accumulator))
    else:
        flag2 = False

    return (accumulator, flag2)


def replace_values(lines):
    accumulator = 0

    new_lines = lines.copy()
    tab = []

    flag = True

    j = 0

    while j < len(lines) and flag:

        code = new_lines[j][0]
        number = int(new_lines[j][1])

        new = lines.copy()

        if code == "nop":
            new_lines[j][0] = "jmp"

            if check(new_lines)[1]:
                flag = False

            else:
                new_lines[j][0] = "nop"

        if code == "jmp":
            new_lines[j][0] = "nop"
            if check(new_lines)[1]:
                flag = False

            else:
                new_lines[j][0] = "jmp"

        new_lines[j] = [new_lines[j][0], str(number)]

        j += 1

    return new_lines


lines = open_file()

task1, _ = check(lines)
print("Accumulator task1: {}".format(task1))

task2 = replace_values(lines)
