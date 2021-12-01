filename = 'text.txt'

with open(filename, 'r') as file:
    Lines = file.readlines()
    NewLines = []

    for line in Lines:
        line = line.rstrip()
        NewLines.append(int(line))

    for x in NewLines:
        for y in NewLines:
            for z in NewLines:
                add = x+y+z
                if add == 2020:
                    multiply = x*y*z
    print(multiply)

