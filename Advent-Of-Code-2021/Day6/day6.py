def get_data():
    with open("puzzle.txt") as file:
        data = [int(x) for x in file.read().split(",")]
    return data


def count_fish(data):
    fish_list = data.copy()
    stop = 0
    while(stop<256):
        new_fish = []
        for fish in fish_list:
            if fish == 0:
                new_fish.append(6)
                new_fish.append(8)
            else:
                new_fish.append(fish-1)
                
        fish_list = new_fish
        stop+=1
            
    return len(fish_list)
        
print(count_fish(get_data()))