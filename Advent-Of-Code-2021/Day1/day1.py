def get_data():
    with open("puzzle.txt", "r") as file:
        data = file.readlines()
        data = [int(line.strip()) for line in data]
    return data


def check_increase(data=get_data()):
    increase = 0
    for icr in range(len(data)-1):
        increase = increase + 1 if data[icr] < data[icr+1] else increase
    return increase


def list_append(data=get_data()):
    A = [data[icr] + data[icr+1] + data[icr+2] for icr in range(len(data)-2)]
    return A


print("Part one: ", check_increase())
print("Part two: ", check_increase(list_append()))
