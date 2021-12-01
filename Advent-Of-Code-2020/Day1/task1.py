filename = 'text.txt'

with open(filename, 'r') as file:
    Lines = file.readlines()
    NewLines = [] 

    line = [line.rstrip() for line in Lines]    

    print(line)

    for line in Lines:
        NewLines.append(int(line))

    #print(NewLines)
    

    for x in NewLines:
        for y in NewLines:
            add = x+y
            if add == 2020:
                multiply = x*y
    print(multiply)
