def get_data():
    with open("puzzle.txt") as file:
        data = [int(x) for x in file.read().split(",")]
    return data


def add_elements(start, end):
    steps = start-end
    add_to_fuel = 0

    if steps < 0:
        steps *= (-1)

    for i in range(steps):
        add_to_fuel += i+1

    return add_to_fuel


def count_fuel(data):
    possible_fuels = list(range(1000))

    basic_fuel = 0
    basic_fuel_list = []
    extended_fuel = 0
    extended_fuel_list = []

    for j in possible_fuels:
        for i in data:
            if i-j < 0:
                basic_fuel += (i - j)*(-1)
            else:
                basic_fuel += i-j
            extended_fuel += add_elements(i, j)

        basic_fuel_list.append(basic_fuel)
        extended_fuel_list.append(extended_fuel)
        basic_fuel = 0
        extended_fuel = 0

    return (min(basic_fuel_list), min(extended_fuel_list))


basic, extended = count_fuel(get_data())
print("Basic {}\nExtended {}".format(basic, extended))
