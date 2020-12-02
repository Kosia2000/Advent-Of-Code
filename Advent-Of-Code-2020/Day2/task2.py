def bad_pass(filename):
    file = open(filename, "r")
    sum = 0
    lines = 0
    for l in file.readlines():
        lines += 1
        rules, letter, password = l.split(" ")
        min, max = rules.split("-")
        letter = letter[0]
        pswd = password.strip()

        if pswd[int(min)-1] != letter and pswd[int(max)-1] == letter:
            print("Password correct")
        elif pswd[int(min)-1] == letter and pswd[int(max)-1] != letter:
            print("Password correct")
        else:
            sum += 1

    print(lines)
    print("Correct passwords: {} ".format(lines-sum))

    file.close()


bad_pass("text.txt")
