filename = 'text.txt'

file = open(filename, 'r')

Lines = file.readlines()

file.close()

Lines = [line.strip() for line in Lines]


def count_trees(Lines, right, down):
    rows = 0
    columns = 0
    trees = 0

    while rows + 1 < len(Lines):
        columns += right
        rows += down

        hash = Lines[rows][columns % len(Lines[rows])]
        if hash == "#":
            trees += 1
    return trees


print("Right 1, down 1: {}".format(count_trees(Lines, 1,1)))
print("Right 3, down 1: {}".format(count_trees(Lines, 3,1)))
print("Right 5, down 1: {}".format(count_trees(Lines, 5,1)))
print("Right 7, down 1: {}".format(count_trees(Lines, 7,1)))
print("Right 1, down 2: {}".format(count_trees(Lines, 1,2)))

total = 58*223*105*74*35
print(total)
