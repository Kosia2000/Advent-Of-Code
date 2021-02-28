def get_data():
    with open('text.txt') as file:
        data = file.readlines()
        data = [int(line.strip()) for line in data]
        return data


def fix_list(new_data):
    new_data.append(0)
    new_data.append(max(new_data)+3)
    new_data.sort()
    return new_data


def count_difference():
    numbers = fix_list(get_data())
    byOne = 0
    byThree = 0

    for nr in range(len(numbers)-1):
        difference = numbers[nr+1] - numbers[nr]
        if difference == 1:
            byOne += 1
        elif difference == 3:
            byThree += 1

    return byOne * byThree


checked = {}

def get_way(position=0):
    all = 0
    data = fix_list(get_data())

    if position == len(data)-1:
        return 1

    if position in checked:
        return checked[position]

    for i in range(position+1, len(data)):
        if data[i] - data[position] <= 3:
            all += get_way(i)

    checked[position] = all
    return all


print("Part one: {}".format(count_difference()))
print("Part two: {}".format(get_way()))
