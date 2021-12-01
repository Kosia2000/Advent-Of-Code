def bad_pass(filename):
    file = open(filename, "r")
    sum_quantity = 0
    lines = 0
    for l in file.readlines():
        lines += 1
        rules, letter, password = l.split(" ")
        start, end = rules.split("-")
        letter = letter[0]
        pswd = password.strip()

        if pswd[int(start)-1] != letter and pswd[int(end)-1] == letter:
            print("Password correct")
        elif pswd[int(start)-1] == letter and pswd[int(end)-1] != letter:
            print("Password correct")
        else:
            sum_quantity += 1

    print(lines)
    print("Correct passwords: {} ".format(lines-sum_quantity))

    file.close()


bad_pass("text.txt")
