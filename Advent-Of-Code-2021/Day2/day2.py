def get_data():
    data = []
    with open("puzzle.txt", "r") as file:
        data = [i.strip().split(" ") for i in file.readlines()]
    return data


def count_data(data):
    depth = 0
    horizontal = 0
    for elements in range(len(data)):
        key = data[elements][0]
        value = int(data[elements][1])

        if key == "forward":
            horizontal += value

        elif key == "down":
            depth += value
        else:
            depth -= value
    return (horizontal*depth)


def count_data_aim(data):
    depth = 0
    horizontal = 0
    aim = 0
    for elements in range(len(data)):
        key = data[elements][0]
        value = int(data[elements][1])

        if key == "forward":
            horizontal += value
            depth += (aim*value)
        elif key == "down":
            aim += value
        else:
            aim -= value

    return (horizontal*depth)


print(count_data(get_data()))
print(count_data_aim(get_data()))
