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

        quantity = pswd.count(letter)

        if quantity < int(min) or quantity > int(max):
            sum += 1

    print("\nCorrect passwords = ", lines-sum)

    file.close()


bad_pass("text.txt")
