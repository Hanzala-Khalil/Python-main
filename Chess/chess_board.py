from enter_move import Move 

BOARD = [
    ["♜",
     "♞",
     "♝",
     "♛",
     "♚",
     "♝",
     "♞",
     "♜"],
    ["♟",
     "♟",
     "♟",
     "♟",
     "♟",
     "♟",
     "♟",
     "♟"],
    [" ",
     " ",
     " ",
     " ",
     " ",
     " ",
     " ",
     " "],
    [" ",
     " ",
     " ",
     " ",
     " ",
     " ",
     " ",
     " "],
    [" ",
     " ",
     " ",
     " ",
     " ",
     " ",
     " ",
     " "],
    [" ",
     " ",
     " ",
     " ",
     " ",
     " ",
     " ",
     " "],
    ["♙",
     "♙",
     "♙",
     "♙",
     "♙",
     "♙",
     "♙",
     "♙"],
    ["♖",
     "♘",
     "♗",
     "♕",
     "♔",
     "♗",
     "♘",
     "♖"]]
board=[[" " for i in range(8)] for j in range(8)]

def print_board():
    print("       A        B        C        D        E        F        G        H    " )
    for i,n in enumerate(range(8,0,-1)):
        print("    -------- -------- -------- -------- -------- -------- -------- --------" )
        for j in range(0,8): 
            print("   |    ", end=" ")
        print(f"   |\n{n}", end=" ")
        for j in range(0,8): 
            print(f" |   {board[i][j]}  ", end=" ")
        print(f" |  {n}")
        for j in range(0,8): 
            print("   |    ", end=" ")
        print("   |")
    print("    -------- -------- -------- -------- -------- -------- -------- --------")
    print("       A        B        C        D        E        F        G        H    \n")
    Move() 

