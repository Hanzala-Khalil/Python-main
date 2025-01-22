import os
import chess_board as cb

counter = 0

def New_Game():
    counter = 0;
    for i in range(8):
        for j in range(8):
            cb.board[i][j]=cb.BOARD[i][j]
    cb.print_board()
    


def main():

    choice = 0

    print("\n1.New Game")
    print("\n2.Load Game")
    print("\n3.Save Game")
    print("\n4.Exit")


    choice = input("\n\tEnter Choice: ")
    if choice == "1":
        os.system('cls')
        New_Game()
    elif choice == "2":
        print("Load")
    elif choice == "3":
        print("Save")
    elif choice == "4":
        os.system('cls')
        print("\n\n\tThank You!!") 
    else:
        os.system('cls')
        print("\n\tError:Invalid Choice \n\n\tTry Again")
        main()          


main()

