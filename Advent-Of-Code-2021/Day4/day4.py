def get_data():
    bingo_boards = []
    with open("my_data.txt") as file:
        my_numbers = [int(x) for x in file.read().split(",")]

    with open("bingo_data.txt") as file:
        
        bingo_numbers = file.read().split()
        for i in range(0,len(bingo_numbers),25):
            bingo_boards.append(BingoBoard(bingo_numbers[i:i+25:1]))
        
                
    return (my_numbers,bingo_boards)

class BingoBoard:
    def __init__(self, board_data):
        self.board = [[x,0] for x in board_data]

    def mark_number(self, number):
        for mark in self.board:
            if number == mark[0]:
                mark[1] = 1
            

    def check_bingo(self):
        if self.check_row() or self.check_column():
            return True
        else:
            return False

    def check_row(self):
        row_bingo = False
        for i in range(0,21,5):
            counter = 0
            for row_value in self.board[i:i+5]:
                if row_value[1] == 1:
                    counter+=1
            if counter == 5:
                row_vingo = True

        return row_bingo
                

    def check_column(self):
        column_bingo = False
        for i in range(5):
            counter = 0
            for column_value in self.board[i:i+21:5]:
                if column_value[1] == 1:
                    counter+=1
            if counter == 5:
                column_bingo = True
        return column_bingo   

    def count_unmarked(self):
        counter = 0
        for number in self.board:
            if number[1] == 0:
                counter+=int(number[0])
        return counter

       


numbers, boards = get_data()

def play_bingo(numbers, boards):
    for number in numbers:
        number = str(number)
        for board in boards:
            board.mark_number(number)

            is_bingo = board.check_bingo()
            if is_bingo:
                return board.count_unmarked() * int(number)
    

print(play_bingo(numbers, boards))

