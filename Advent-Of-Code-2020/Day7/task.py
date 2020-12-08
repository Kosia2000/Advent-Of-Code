filename = 'text.txt'


def open_file():
    lines = []
    with open(filename, "r") as file:
        data = file.readlines()
        lines = [line.strip().split() for line in data]
    return lines


def _check():
    lines = open_file()
    acumulator = 0
    i = 0

    used_commands = []
    flag = True

    while flag:
        code = lines[i][0]
        number = int(lines[i][1])

        if i not in used_commands:

            if code == "acc":
                acumulator += number
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

    print("Acumulator: {}".format(acumulator))


_check()
