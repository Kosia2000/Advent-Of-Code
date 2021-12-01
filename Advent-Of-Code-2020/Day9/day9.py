with open("text.txt") as file:
    data = file.readlines()
    data = [int(line.strip()) for line in data]


def number_fun():
    lenght1 = len(data)

    flag2 = True
    if flag2:
        for x in range(25, lenght1):
            number = data[x-25:x]
            curr_number = data[x]

            flag = True
            wrong = False

            for y in range(len(number)+1):
                if flag:
                    for z in range(y+1, len(number)):
                        if number[y]+number[z] == curr_number:
                            flag = False
                            wrong = True

            if wrong == True:
                continue

            return curr_number


def get_key():
    wrong = False
    first_num = number_fun()

    for x in range(len(data)-1):
        nums = [data[x]]
        flag = True

        for y in range(x+1, len(data)):
            if flag:
                nums.append(data[y])
                suma = sum(nums)

            if suma == first_num:
                wrong = True
                flag = False

            elif suma > first_num:
                flag = False

        if wrong == True:
            break

    return min(nums)+max(nums)


print("Part one: {}".format(number_fun()))

print("Part two: {}".format(get_key()))
