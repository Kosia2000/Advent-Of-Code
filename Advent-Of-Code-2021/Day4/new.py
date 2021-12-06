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

    def markNumber(self, number):
        for mark in self.board:
            if number == mark[0]:
                mark[1] = 1
            

    def checkBingo(self):
        if self.checkRow() or self.checkColumn():
            return True
        else:
            return False

    def checkRow(self):
        rowBingo = False
        for i in range(0,21,5):
            counter = 0
            for rowValue in self.board[i:i+5]:
                if rowValue[1] == 1:
                    counter+=1
            if counter == 5:
                rowBingo = True

        return rowBingo
                

    def checkColumn(self):
        columnBingo = False
        for i in range(5):
            counter = 0
            for columnValue in self.board[i:i+21:5]:
                if columnValue[1] == 1:
                    counter+=1
            if counter == 5:
                columnBingo = True
        return columnBingo   

    def countUnmarked(self):
        counter = 0
        for number in self.board:
            if number[1] == 0:
                counter+=int(number[0])
        return counter

       


numbers, boards = get_data()

def playBingo(numbers, boards):
    for number in numbers:
        number = str(number)
        for board in boards:
            board.markNumber(number)

            isBingo = board.checkBingo()
            if isBingo:
                return board.countUnmarked() * int(number)
    

print(playBingo(numbers, boards))

