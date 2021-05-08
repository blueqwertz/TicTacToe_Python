board = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def printBoard(board):
    output = ""

    for i in range(9):
        if (i + 1) % 3 == 0 and i != 0:
            if type(board[i]) == int:
                output += " | " + str(board[i]) + " |\n"
            else:
                output += f" | {bcolors.OKGREEN}{bcolors.BOLD}{board[i]}{bcolors.ENDC} |\n"
        else:
            if type(board[i]) == int:
                output += " | " + str(board[i]) + ""
            else:
                output += f" | {bcolors.OKGREEN}{bcolors.BOLD}{board[i]}{bcolors.ENDC}"
    return output

def check(arr, player):
    board = [arr[0:3], arr[3:6], arr[6:9]]
    for row in range(0, 3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != 0:
            if board[row][0] == player:
                return 10
            return -10
    for col in range(0, 3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            if board[0][col] == player:
                return 10
            return -10
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        if board[0][0] == player:
            return 10
        return -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        if board[0][2] == player:
            return 10
        return -10
    if len(find(arr)) > 0:
        return None
    return 0


curplayer = 1
player = 0
engine = 1

sign = ["O", "X"]


def find(board):
    pos = []
    for i in range(len(board)):
        if type(board[i]) == int:
            pos.append(i)
    return pos


def search():
    def minMax(board, isMax, depth):
        score = check(board, sign[engine])
        if score is not None:
            return score - depth
        moves = find(board)
        # AI = X
        if isMax:
            bestScore = -1
            for position in moves:
                board[position] = sign[engine]
                bestScore = max(bestScore, minMax(board, False, depth + 1))
                board[position] = position + 1
            return bestScore
        # Human = O
        else:
            worstScore = 1
            for position in moves:
                board[position] = sign[player]
                worstScore = min(worstScore, minMax(board, True, depth + 1))
                board[position] = position + 1
            return worstScore

    moves = find(board)
    bestVal = -999999
    bestMove = None
    for move in moves:
        board[move] = sign[engine]
        score = minMax(board, False, 1)
        board[move] = move + 1
        if score > bestVal:
            bestVal = score
            bestMove = move
    return bestMove


# start = input("Do you want to start(y/n):")
# if start == "n":
#     curplayer = 1

while True:
    if curplayer == engine:
        move = search()
        print("CPU selected field", move + 1)
        board[move] = sign[engine]
    else:
        try:
            field = int(input(f"{printBoard(board)}Select Field (1-9): ")) - 1
        except:
            print("Invalid Input!")
            continue
        while type(board[field]) != int:
            try:
                field = int(input("Field already set. Select another Field (1-9): ")) - 1
            except:
                print("Invalid Input!")
                continue
        board[field] = sign[player]
    curplayer = 1 - curplayer
    score = check(board, sign[engine])
    if score != None:
        print(printBoard(board))
        if score == 10:
            print("CPU won!")
        elif score == -10:
            print("YOU won!")
        else:
            print("Draw")
        if input("Play again? (y/n): ").lower() != "n":
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            curplayer = 1
        else:
            break