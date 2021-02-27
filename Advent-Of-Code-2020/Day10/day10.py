def get_data():
    with open('text.txt') as file:
        data = file.readlines()
        data = [int(line.strip()) for line in data]
        return data


def fix_list():
    new_data = get_data()
    new_data.append(0)
    new_data.append(max(new_data)+3)
    new_data.sort()
    return new_data


def count_difference():
    numbers = fix_list()
    byOne = 0
    byThree = 0

    for nr in range(len(numbers)-1):
        difference = numbers[nr+1] - numbers[nr]
        if difference == 1:
            byOne += 1
        elif difference == 3:
            byThree += 1

    return byOne * byThree

print("Part one: {}".format(count_difference()))
