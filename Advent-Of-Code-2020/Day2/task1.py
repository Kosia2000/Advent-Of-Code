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

        quantity = pswd.count(letter)

        if quantity < int(start) or quantity > int(end):
            sum_quantity += 1

    print("\nCorrect passwords = ", lines-sum_quantity)

    file.close()


bad_pass("text.txt")
