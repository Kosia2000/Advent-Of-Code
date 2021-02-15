with open("input.txt") as file:
    data = file.readlines()
    cardKey = int(data[0].strip())
    doorKey = int(data[1].strip())

def loop_count():
    loop_counter = 0
    x = 1
    while x != cardKey:
        loop_counter += 1
        x = (x*7)%20201227
    return loop_counter

def good_key(counter):
    newKey = 1
    for count in range(counter):
        newKey = (newKey * doorKey) % 20201227
    print(newKey)

counter = loop_count()
good_key(counter)