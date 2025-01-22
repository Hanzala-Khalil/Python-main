def Move():
    col,row= input("\n\nEnter Move: "),int(input()) 

    scanf("%c%c%d%c%c%d", &temp, &col[0], &row[0], &col[1], &col[1], &row[1]) 

    if (col[1] == col[0] && row_i[1] == row[0])
    {
        print("ERROR : SAME CELL") 
        goto Main 
    }

    // GIVING COUNTER INDEX

    if (counter % 2 == 0)
    {
        counter_i = 1 
    }
    else
    {
        counter_i = 2 
    }

    // GIVING COLUMN INDEX

    for (int i = 0  i < 2  i++)
    {
        int letter[2] = {65, 97} 
        for (int j = 0  j < 8  j++)
        {
            if (col[i] == letter[0] || col[i] == letter[1])
            {
                col_i[i] = j 
                break 
            }
            else if (j == 7)
            {
                print("ERROR : INVALID COLUMN\n") 
                goto Main 
            }
            letter[0]++ 
            letter[1]++ 
        }
    }

    // GIVING ROW INDEX

    for (int i = 0  i < 2  i++)
    {
        if (row[i] < 1 || row[i] > 8)
        {
            print("ERROR : INVALID ROW\n") 
            goto Main 
        }
        else
        {
            row_i[i] = row[i] - 1 
        }
    }

    // CHECKING PIECE COLOR

    if (board_info[row_i[0]][col_i[0]][1] == 0)
    {
        print("ERROR : EMPTY CELL\n") 
        goto Main 
    }
    else if (board_info[row_i[0]][col_i[0]][1] != counter_i)
    {
        print("ERROR : OPPONENTS PIECE\n") 
        goto Main 
    }

    // GIVING PIECE INDEX

    if (strcmp(board[row_i[0]][col_i[0]][0], "♚") == 0 || strcmp(board[row_i[0]][col_i[0]][0], "♔") == 0)
    {
        piece_i = 6 
    }
    else if (strcmp(board[row_i[0]][col_i[0]][0], "♛") == 0 || strcmp(board[row_i[0]][col_i[0]][0], "♕") == 0)
    {
        piece_i = 5 
    }
    else if (strcmp(board[row_i[0]][col_i[0]][0], "♝") == 0 || strcmp(board[row_i[0]][col_i[0]][0], "♗") == 0)
    {
        piece_i = 4 
    }
    else if (strcmp(board[row_i[0]][col_i[0]][0], "♞") == 0 || strcmp(board[row_i[0]][col_i[0]][0], "♘") == 0)
    {
        piece_i = 3 
    }
    else if (strcmp(board[row_i[0]][col_i[0]][0], "♜") == 0 || strcmp(board[row_i[0]][col_i[0]][0], "♖") == 0)
    {
        piece_i = 2 
    }
    else if (strcmp(board[row_i[0]][col_i[0]][0], "♟") == 0 || strcmp(board[row_i[0]][col_i[0]][0], "♙") == 0)
    {
        piece_i = 1 
    }
    else
    {
        piece_i = 0 
        print("ERROR : EMPTY SQUARE\n") 
        goto Main 
    }

    // CALLING FUNCTION TO CHECK POSSIBLE MOVES

    if (piece_i == board_info[row_i[0]][col_i[0]][2])
    {
        switch (counter_i)
        {
        case 1:
            switch (piece_i)
            {
            case 6:
                print("king_w") 
                break 
            case 5:
                print("queen_w") 
                break 
            case 4:
                Bishop_W() 
                break 
            case 3:
                print("knight_w") 
                break 
            case 2:
                Rook_W() 
                break 
            case 1:
                Pawn_W() 
                break 
            }
        case 2:
            switch (piece_i)
            {
            case 6:
                print("king_b") 
                break 
            case 5:
                print("queen_b") 
                break 
            case 4:
                Bishop_B() 
                break 
            case 3:
                print("knight_b") 
                break 
            case 2:
                Rook_B() 
                break 
            case 1:
                Pawn_B() 
                break 
            }
        default:
            break 
        }
    }
    else
    {
        system("clear") 
        print("ERROR : PROGRAM CRASHED ") 
    }
}

