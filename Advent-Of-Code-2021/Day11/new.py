GRID = 10


def get_data():
    data = []
    for line in open("puzzle.txt"):
        data.append([int(x) for x in line.strip()])
    return data


flashes = 0


def flash(hor, ver, data):
    global flashes
    flashes += 1
    data[hor][ver] = -1

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            hor_flash = hor + i
            ver_flash = ver + j

            if 0 <= hor_flash < GRID and 0 <= ver_flash < GRID:
                if data[hor_flash][ver_flash] != -1:
                    data[hor_flash][ver_flash] += 1
                    if data[hor_flash][ver_flash] >= 10:
                        flash(hor_flash, ver_flash, data)
    return flashes


def loop_octopuses(data):
    step = 0
    octopuses = 100
    while octopuses:
        all_flash = True
        step += 1
        for hor in range(GRID):
            for ver in range(GRID):
                data[hor][ver] += 1

        for hor in range(GRID):
            for ver in range(GRID):
                if data[hor][ver] > 9:
                    flashes = flash(hor, ver, data)

        if step == 100:
            print(flashes)

        for hor in range(GRID):
            for ver in range(GRID):
                if data[hor][ver] == -1:
                    data[hor][ver] = 0
                else:
                    all_flash = False

        if all_flash:
            print(step)
            octopuses -= 100


loop_octopuses(get_data())
