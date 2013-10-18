## This computer program is free software. It is licensed for use under the GNU
## GENERAL PUBLIC LICENSE Version 3.



import random



def new_game():
    chess_board = (           
                  '**********' ,
                  '*rnbqkbnr*' ,  
                  '*pppppppp*' ,
                  '*--------*' ,
                  '*--------*' ,
                  '*--------*' ,
                  '*--------*' ,
                  '*PPPPPPPP*' , 
                  '*RNBQKBNR*' ,
                  '**********'
                  )
    chess_board = "".join(reversed(chess_board))
    newgame = chess_board + '0#0#0#0#0#0#0#KQkq#00'
    return newgame



def white_king(square, board):
    """Move generator for the white king that returns a list of all its possible
    moves
    """
    moves = []
    #0-degree bearing       
    if (square + 10) < 100:
        if board[square + 10] == "-":  
           move = "K" + "-" + str(square) + "-" + str(square + 10)
           moves.append(move)
        if board[square + 10].islower(): 
           move = "K" + "-" + str(square) + "x" + str(square + 10)
           moves.append(move)
    #45-degree bearing       
    if (square + 11) < 100:
        if board[square + 11] == "-":  
           move = "K" + "-" + str(square) + "-" + str(square + 11)
           moves.append(move)
        if board[square + 11].islower(): 
           move = "K" + "-" + str(square) + "x" + str(square + 11)
           moves.append(move)
    #90-degree bearing       
    if (square + 1) < 100:
        if board[square + 1] == "-":  
           move = "K" + "-" + str(square) + "-" + str(square + 1)
           moves.append(move)
    if (square + 1) < 100:
        if board[square + 1].islower(): 
           move = "K" + "-" + str(square) + "x" + str(square + 1)
           moves.append(move)    
    #135-degree bearing       
    if (square - 9) > 0:
        if board[square - 9] == "-":  
           move = "K" + "-" + str(square) + "-" + str(square - 9)
           moves.append(move)
    if (square - 9) > 0:
        if board[square - 9].islower(): 
           move = "K" + "-" + str(square) + "x" + str(square - 9)
           moves.append(move)
    #180-degree bearing       
    if (square - 10) > 0:
        if board[square - 10] == "-":  
           move = "K" + "-" + str(square) + "-" + str(square - 10)
           moves.append(move)
    if (square - 10) > 0:
        if board[square - 10].islower(): 
           move = "K" + "-" + str(square) + "x" + str(square - 10)
           moves.append(move)
    #225-degree bearing       
    if (square - 11) > 0:
        if board[square - 11] == "-":  
           move = "K" + "-" + str(square) + "-" + str(square - 11)
           moves.append(move)
    if (square - 11) > 0:
        if board[square - 11].islower(): 
           move = "K" + "-" + str(square) + "x" + str(square - 11)
           moves.append(move)
    #270-degree bearing       
    if (square - 1) > 0:
        if board[square - 1] == "-":  
           move = "K" + "-" + str(square) + "-" + str(square - 1)
           moves.append(move)
    if (square - 1) > 0:
        if board[square - 1].islower(): 
           move = "K" + "-" + str(square) + "x" + str(square - 1)
           moves.append(move)
    #315-degree bearing
    if (square + 9) < 100:
        if board[square + 9] == "-":  
           move = "K" + "-" + str(square) + "-" + str(square + 9)
           moves.append(move)
        if board[square + 9].islower(): 
           move = "K" + "-" + str(square) + "x" + str(square + 9)
           moves.append(move)
    #return the list of king moves
    return moves

    

def white_queen(square, board):
    """generates possible moves for the white queen"""  
    moves = []
    #0-degree bearing
    count = 10
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        #emtpy square
        if board[square + count] == "-":
            move = "Q" + "-" + str(square) + "-" + str(square + count)
            moves.append(move)
        if board[square + count].islower(): 
            move = "Q" + "-" + str(square) + "x" + str(square + count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square + count].islower() or board[square + count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 10
    #45-degree bearing
    count = 11
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square + count] == "-":
            move = "Q" + "-" + str(square) + "-" + str(square + count)
            moves.append(move)
        if board[square + count].islower(): 
            move = "Q" + "-" + str(square) + "x" + str(square + count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square + count].islower() or board[square + count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 11
    #90-degree bearing
    count = 1
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square + count] == "-":
            move = "Q" + "-" + str(square) + "-" + str(square + count)
            moves.append(move)
        if board[square + count].islower(): 
            move = "Q" + "-" + str(square) + "x" + str(square + count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square + count].islower() or board[square + count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 1
    #135-degree bearing
    count = 9
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square - count] == "-":
            move = "Q" + "-" + str(square) + "-" + str(square - count)
            moves.append(move)
        if board[square - count].islower(): 
            move = "Q" + "-" + str(square) + "x" + str(square - count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square - count].islower() or board[square - count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 9
    #180-degree bearing
    count = 10
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square - count] == "-":
            move = "Q" + "-" + str(square) + "-" + str(square - count)
            moves.append(move)
        if board[square - count].islower(): 
            move = "Q" + "-" + str(square) + "x" + str(square - count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square - count].islower() or board[square - count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 10
    #225-degree bearing
    count = 11
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square - count] == "-":
            move = "Q" + "-" + str(square) + "-" + str(square - count)
            moves.append(move)
        if board[square - count].islower(): 
            move = "Q" + "-" + str(square) + "x" + str(square - count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square - count].islower() or board[square - count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 11
    #270-degree bearing
    count = 1
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square - count] == "-":
            move = "Q" + "-" + str(square) + "-" + str(square - count)
            moves.append(move)
        if board[square - count].islower(): 
            move = "Q" + "-" + str(square) + "x" + str(square - count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square - count].islower() or board[square - count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 1
    #315-degree bearing
    count = 9
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square + count] == "-":
            move = "Q" + "-" + str(square) + "-" + str(square + count)
            moves.append(move)
        if board[square + count].islower(): 
            move = "Q" + "-" + str(square) + "x" + str(square + count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square + count].islower() or board[square + count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 9
    #return the list of queen moves
    return moves



#knight move-generator for white
def white_knight(square, board):  
    moves = []
    #30-degree bearing       
    if (square + 21) < 100:
        if board[square + 21] == "-":  
           move = "N" + "-" + str(square) + "-" + str(square + 21)
           moves.append(move)
    if (square + 21) < 100:
        if board[square + 21].islower(): 
           move = "N" + "-" + str(square) + "x" + str(square + 21)
           moves.append(move)
    #60-degree bearing       
    if (square + 12) < 100:
        if board[square + 12] == "-":  
           move = "N" + "-" + str(square) + "-" + str(square + 12)
           moves.append(move)
    if (square + 12) < 100:
        if board[square + 12].islower(): 
           move = "N" + "-" + str(square) + "x" + str(square + 12)
           moves.append(move)
    #120-degree bearing               
    if (square - 8) > 0:
        if board[square - 8] == "-":  
           move = "N" + "-" + str(square) + "-" + str(square - 8)
           moves.append(move)
    if (square - 8) > 0:
        if board[square - 8].islower(): 
           move = "N" + "-" + str(square) + "x" + str(square - 8)
           moves.append(move)
    #150-degree bearing
    if (square - 19) > 0:
        if board[square - 19] == "-":  
           move = "N" + "-" + str(square) + "-" + str(square - 19)
           moves.append(move)
    if (square - 19) > 0:
        if board[square - 19].islower(): 
           move = "N" + "-" + str(square) + "x" + str(square - 19)
           moves.append(move)
    #210-degree bearing
    if (square - 21) > 0:
        if board[square - 21] == "-":  
           move = "N" + "-" + str(square) + "-" + str(square - 21)
           moves.append(move)
    if (square - 21) > 0:
        if board[square - 21].islower(): 
           move = "N" + "-" + str(square) + "x" + str(square - 21)
           moves.append(move)
    #240-degree bearing
    if (square - 12) > 0:
        if board[square - 12] == "-":  
           move = "N" + "-" + str(square) + "-" + str(square - 12)
           moves.append(move)
    if (square - 12) > 0:
        if board[square - 12].islower(): 
           move = "N" + "-" + str(square) + "x" + str(square - 12)
           moves.append(move)
    #300-degree bearing
    if (square + 8) < 100:
        if board[square + 8] == "-":  
           move = "N" + "-" + str(square) + "-" + str(square + 8)
           moves.append(move)
    if (square + 8) < 100:
        if board[square + 8].islower(): 
           move = "N" + "-" + str(square) + "x" + str(square + 8)
           moves.append(move)
    #330-degree bearing       
    if (square + 19) < 100:
        if board[square + 19] == "-":  
           move = "N" + "-" + str(square) + "-" + str(square + 19)
           moves.append(move)
    if (square + 19) < 100:
        if board[square + 19].islower(): 
           move = "N" + "-" + str(square) + "x" + str(square + 19)
           moves.append(move)
    #return list of knight moves
    return moves 


#pawn move-generator for white           
def white_pawn(square, board):  
    moves = []
    #0-degree bearing
    if board[square + 10] == "-":  
        move = "P" + "-" + str(square) + "-" + str(square + 10)
        moves.append(move)
        #two-step move that a pawn can begin with
        if square in range(20, 29) and board[square + 20] == "-":  
            move = "P" + "-" + str(square) + "-" + str(square + 20)
            moves.append(move)
    #45-degree bearing capture
    if board[square + 11].islower():  
        move = "P" + "-" + str(square) + "x" + str(square + 11)
        moves.append(move)
    #315-degree bearing capture
    if board[square + 9].islower():  
        move = "P" + "-" + str(square) + "x" + str(square + 9)
        moves.append(move)             
    #return list of pawn moves
    return moves


#rook move-generator for white
def white_rook(square, board):  
    moves = []
    #0-degree bearing
    count = 10
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square + count] == "-":
            move = "R" + "-" + str(square) + "-" + str(square + count)
            moves.append(move)
        if board[square + count].islower(): 
            move = "R" + "-" + str(square) + "x" + str(square + count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square + count].islower() or board[square + count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 10
    #90-degree bearing
    count = 1
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square + count] == "-":
            move = "R" + "-" + str(square) + "-" + str(square + count)
            moves.append(move)
        if board[square + count].islower(): 
            move = "R" + "-" + str(square) + "x" + str(square + count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square + count].islower() or board[square + count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 1
    #180-degree bearing
    count = 10
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square - count] == "-":
            move = "R" + "-" + str(square) + "-" + str(square - count)
            moves.append(move)
        if board[square - count].islower(): 
            move = "R" + "-" + str(square) + "x" + str(square - count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square - count].islower() or board[square - count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 10
    #270-degree bearing
    count = 1
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square - count] == "-":
            move = "R" + "-" + str(square) + "-" + str(square - count)
            moves.append(move)
        if board[square - count].islower(): 
            move = "R" + "-" + str(square) + "x" + str(square - count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square - count].islower() or board[square - count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 1
    #return list of rook moves
    return moves             
    

#bishop move-generator for white
def white_bishop(square, board):  
    moves = []
    #45-degree bearing
    count = 11
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square + count] == "-":
            move = "B" + "-" + str(square) + "-" + str(square + count)
            moves.append(move)
        if board[square + count].islower(): 
            move = "B" + "-" + str(square) + "x" + str(square + count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square + count].islower() or board[square + count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 11
    #135-degree bearing
    count = 9
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square - count] == "-":
            move = "B" + "-" + str(square) + "-" + str(square - count)
            moves.append(move)
        if board[square - count].islower(): 
            move = "B" + "-" + str(square) + "x" + str(square - count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square - count].islower() or board[square - count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 9
    #225-degree bearing
    count = 11
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square - count] == "-":
            move = "B" + "-" + str(square) + "-" + str(square - count)
            moves.append(move)
        if board[square - count].islower(): 
            move = "B" + "-" + str(square) + "x" + str(square - count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square - count].islower() or board[square - count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 11
    #315-degree bearing
    count = 9
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square + count] == "-":
            move = "B" + "-" + str(square) + "-" + str(square + count)
            moves.append(move)
        if board[square + count].islower(): 
            move = "B" + "-" + str(square) + "x" + str(square + count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square + count].islower() or board[square + count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 9
    #return list of bishop moves
    return moves   
 
 
#king move-generator for black
def black_king(square, board):  
    moves = []
    #0-degree bearing       
    if (square + 10) < 100:
        if board[square + 10] == "-":  
           move = "k" + "-" + str(square) + "-" + str(square + 10)
           moves.append(move)
        if board[square + 10].isupper(): 
           move = "k" + "-" + str(square) + "x" + str(square + 10)
           moves.append(move)
    #45-degree bearing       
    if (square + 11) < 100:
        if board[square + 11] == "-":  
           move = "k" + "-" + str(square) + "-" + str(square + 11)
           moves.append(move)
        if board[square + 11].isupper(): 
           move = "k" + "-" + str(square) + "x" + str(square + 11)
           moves.append(move)
    #90-degree bearing       
    if (square + 1) < 100:
        if board[square + 1] == "-":  
           move = "k" + "-" + str(square) + "-" + str(square + 1)
           moves.append(move)
    if (square + 1) < 100:
        if board[square + 1].isupper(): 
           move = "k" + "-" + str(square) + "x" + str(square + 1)
           moves.append(move)    
    #135-degree bearing       
    if (square - 9) > 0:
        if board[square - 9] == "-":  
           move = "k" + "-" + str(square) + "-" + str(square - 9)
           moves.append(move)
    if (square - 9) > 0:
        if board[square - 9].isupper(): 
           move = "k" + "-" + str(square) + "x" + str(square - 9)
           moves.append(move)
    #180-degree bearing       
    if (square - 10) > 0:
        if board[square - 10] == "-":  
           move = "k" + "-" + str(square) + "-" + str(square - 10)
           moves.append(move)
    if (square - 10) > 0:
        if board[square - 10].isupper(): 
           move = "k" + "-" + str(square) + "x" + str(square - 10)
           moves.append(move)
    #225-degree bearing       
    if (square - 11) > 0:
        if board[square - 11] == "-":  
           move = "k" + "-" + str(square) + "-" + str(square - 11)
           moves.append(move)
    if (square - 11) > 0:
        if board[square - 11].isupper(): 
           move = "k" + "-" + str(square) + "x" + str(square - 11)
           moves.append(move)
    #270-degree bearing       
    if (square - 1) > 0:
        if board[square - 1] == "-":  
           move = "k" + "-" + str(square) + "-" + str(square - 1)
           moves.append(move)
    if (square - 1) > 0:
        if board[square - 1].isupper(): 
           move = "k" + "-" + str(square) + "x" + str(square - 1)
           moves.append(move)
    #315-degree bearing
    if (square + 9) < 100:
        if board[square + 9] == "-":  
           move = "k" + "-" + str(square) + "-" + str(square + 9)
           moves.append(move)
        if board[square + 9].isupper(): 
           move = "k" + "-" + str(square) + "x" + str(square + 9)
           moves.append(move)
    #return the list of king moves
    return moves
    

#queen move-generator for black 
def black_queen(square, board):  
    moves = []
    #0-degree bearing
    count = 10
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        #emtpy square
        if board[square + count] == "-":
            move = "q" + "-" + str(square) + "-" + str(square + count)
            moves.append(move)
        if board[square + count].isupper(): 
            move = "q" + "-" + str(square) + "x" + str(square + count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square + count].isupper() or board[square + count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 10
    #45-degree bearing
    count = 11
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square + count] == "-":
            move = "q" + "-" + str(square) + "-" + str(square + count)
            moves.append(move)
        if board[square + count].isupper(): 
            move = "q" + "-" + str(square) + "x" + str(square + count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square + count].isupper() or board[square + count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 11
    #90-degree bearing
    count = 1
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square + count] == "-":
            move = "q" + "-" + str(square) + "-" + str(square + count)
            moves.append(move)
        if board[square + count].isupper(): 
            move = "q" + "-" + str(square) + "x" + str(square + count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square + count].isupper() or board[square + count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 1
    #135-degree bearing
    count = 9
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square - count] == "-":
            move = "q" + "-" + str(square) + "-" + str(square - count)
            moves.append(move)
        if board[square - count].isupper(): 
            move = "q" + "-" + str(square) + "x" + str(square - count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square - count].isupper() or board[square - count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 9
    #180-degree bearing
    count = 10
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square - count] == "-":
            move = "q" + "-" + str(square) + "-" + str(square - count)
            moves.append(move)
        if board[square - count].isupper(): 
            move = "q" + "-" + str(square) + "x" + str(square - count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square - count].isupper() or board[square - count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 10
    #225-degree bearing
    count = 11
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square - count] == "-":
            move = "q" + "-" + str(square) + "-" + str(square - count)
            moves.append(move)
        if board[square - count].isupper(): 
            move = "q" + "-" + str(square) + "x" + str(square - count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square - count].isupper() or board[square - count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 11
    #270-degree bearing
    count = 1
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square - count] == "-":
            move = "q" + "-" + str(square) + "-" + str(square - count)
            moves.append(move)
        if board[square - count].isupper(): 
            move = "q" + "-" + str(square) + "x" + str(square - count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square - count].isupper() or board[square - count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 1
    #315-degree bearing
    count = 9
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square + count] == "-":
            move = "q" + "-" + str(square) + "-" + str(square + count)
            moves.append(move)
        if board[square + count].isupper(): 
            move = "q" + "-" + str(square) + "x" + str(square + count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square + count].isupper() or board[square + count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 9
    #return the list of queen moves
    return moves


#knight move-generator for black
def black_knight(square, board):  
    moves = []
    #30-degree bearing       
    if (square + 21) < 100:
        if board[square + 21] == "-":  
           move = "n" + "-" + str(square) + "-" + str(square + 21)
           moves.append(move)
    if (square + 21) < 100:
        if board[square + 21].isupper(): 
           move = "n" + "-" + str(square) + "x" + str(square + 21)
           moves.append(move)
    #60-degree bearing       
    if (square + 12) < 100:
        if board[square + 12] == "-":  
           move = "n" + "-" + str(square) + "-" + str(square + 12)
           moves.append(move)
    if (square + 12) < 100:
        if board[square + 12].isupper(): 
           move = "n" + "-" + str(square) + "x" + str(square + 12)
           moves.append(move)
    #120-degree bearing               
    if (square - 8) > 0:
        if board[square - 8] == "-":  
           move = "n" + "-" + str(square) + "-" + str(square - 8)
           moves.append(move)
    if (square - 8) > 0:
        if board[square - 8].isupper(): 
           move = "n" + "-" + str(square) + "x" + str(square - 8)
           moves.append(move)
    #150-degree bearing
    if (square - 19) > 0:
        if board[square - 19] == "-":  
           move = "n" + "-" + str(square) + "-" + str(square - 19)
           moves.append(move)
    if (square - 19) > 0:
        if board[square - 19].isupper(): 
           move = "n" + "-" + str(square) + "x" + str(square - 19)
           moves.append(move)
    #210-degree bearing
    if (square - 21) > 0:
        if board[square - 21] == "-":  
           move = "n" + "-" + str(square) + "-" + str(square - 21)
           moves.append(move)
    if (square - 21) > 0:
        if board[square - 21].isupper(): 
           move = "n" + "-" + str(square) + "x" + str(square - 21)
           moves.append(move)
    #240-degree bearing
    if (square - 12) > 0:
        if board[square - 12] == "-":  
           move = "n" + "-" + str(square) + "-" + str(square - 12)
           moves.append(move)
    if (square - 12) > 0:
        if board[square - 12].isupper(): 
           move = "n" + "-" + str(square) + "x" + str(square - 12)
           moves.append(move)
    #300-degree bearing
    if (square + 8) < 100:
        if board[square + 8] == "-":  
           move = "n" + "-" + str(square) + "-" + str(square + 8)
           moves.append(move)
    if (square + 8) < 100:
        if board[square + 8].isupper(): 
           move = "n" + "-" + str(square) + "x" + str(square + 8)
           moves.append(move)
    #330-degree bearing       
    if (square + 19) < 100:
        if board[square + 19] == "-":  
           move = "n" + "-" + str(square) + "-" + str(square + 19)
           moves.append(move)
    if (square + 19) < 100:
        if board[square + 19].isupper(): 
           move = "n" + "-" + str(square) + "x" + str(square + 19)
           moves.append(move)
    #return list of knight moves
    return moves 



#pawn move-generator for black           
def black_pawn(square, board):  
    moves = []
    #135-degree bearing capture
    if board[square - 9].isupper():  
        move = "p" + "-" + str(square) + "x" + str(square - 9)
        moves.append(move)
    #180-degree bearing
    if board[square - 10] == "-":  
        move = "p" + "-" + str(square) + "-" + str(square - 10)
        moves.append(move)
        #two-step move that a pawn can begin with
        if square in range(70, 79) and board[square - 20] == "-":  
            move = "p" + "-" + str(square) + "-" + str(square - 20)
            moves.append(move)
    #225-degree bearing capture
    if board[square - 11].isupper():  
        move = "p" + "-" + str(square) + "x" + str(square - 11)
        moves.append(move)
            
    #return list of pawn moves
    return moves



#rook move-generator for black
def black_rook(square, board):  
    moves = []
    #0-degree bearing
    count = 10
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square + count] == "-":
            move = "r" + "-" + str(square) + "-" + str(square + count)
            moves.append(move)
        if board[square + count].isupper(): 
            move = "r" + "-" + str(square) + "x" + str(square + count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square + count].isupper() or board[square + count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 10
    #90-degree bearing
    count = 1
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square + count] == "-":
            move = "r" + "-" + str(square) + "-" + str(square + count)
            moves.append(move)
        if board[square + count].isupper(): 
            move = "r" + "-" + str(square) + "x" + str(square + count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square + count].isupper() or board[square + count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 1
    #180-degree bearing
    count = 10
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square - count] == "-":
            move = "r" + "-" + str(square) + "-" + str(square - count)
            moves.append(move)
        if board[square - count].isupper(): 
            move = "r" + "-" + str(square) + "x" + str(square - count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square - count].isupper() or board[square - count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 10
    #270-degree bearing
    count = 1
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square - count] == "-":
            move = "r" + "-" + str(square) + "-" + str(square - count)
            moves.append(move)
        if board[square - count].isupper(): 
            move = "r" + "-" + str(square) + "x" + str(square - count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square - count].isupper() or board[square - count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 1
    #return list of rook moves
    return moves             
    
    

#bishop move-generator for black
def black_bishop(square, board):  
    moves = []
    #45-degree bearing
    count = 11
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square + count] == "-":
            move = "b" + "-" + str(square) + "-" + str(square + count)
            moves.append(move)
        if board[square + count].isupper(): 
            move = "b" + "-" + str(square) + "x" + str(square + count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square + count].isupper() or board[square + count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 11
    #135-degree bearing
    count = 9
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square - count] == "-":
            move = "b" + "-" + str(square) + "-" + str(square - count)
            moves.append(move)
        if board[square - count].isupper(): 
            move = "b" + "-" + str(square) + "x" + str(square - count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square - count].isupper() or board[square - count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 9
    #225-degree bearing
    count = 11
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square - count] == "-":
            move = "b" + "-" + str(square) + "-" + str(square - count)
            moves.append(move)
        if board[square - count].isupper(): 
            move = "b" + "-" + str(square) + "x" + str(square - count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square - count].isupper() or board[square - count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 11
    #315-degree bearing
    count = 9
    while count < 100:  
        moves_list = []
        moves_list = moves_list + moves
        if board[square + count] == "-":
            move = "b" + "-" + str(square) + "-" + str(square + count)
            moves.append(move)
        if board[square + count].isupper(): 
            move = "b" + "-" + str(square) + "x" + str(square + count)
            moves.append(move)
        #stop walking if you capture or reach a border
        if board[square + count].isupper() or board[square + count] == "*":
            count += 100
        if moves_list == moves:
            count += 100
        count += 9
    #return list of bishop moves
    return moves



#pawn promotion operations
def pawn_promotion(operation, move, moves_list, board, player):

    #confirm if the move involves pawn promotion    
    if operation == "confirm":
        legality = False
        #return true if a pawn can be promoted
        if ("P" in move) and ("8" in move[5:6]):
            legality = True
        if ("p" in move) and ("1" in move[5:6]):
            legality = True
        return legality
        
    #replace pawn promotion moves in the list
    if operation == "replace_moves":
        #white moves
        if player == "0":
            pawn_promotion_moves = []
            moves_to_delete = []
            for member in moves_list:
                if ("P" in member) and ("8" in member[5:6]):
                    moves_to_delete.append(member)
                    pawn_promotion_moves.append(member + "=N")
                    pawn_promotion_moves.append(member + "=B")
                    pawn_promotion_moves.append(member + "=R")
                    pawn_promotion_moves.append(member + "=Q")
            if len(moves_to_delete) > 0:
                for member in moves_to_delete:
                    moves_list.remove(member)    
            moves_list += pawn_promotion_moves
            return moves_list
        #black moves
        if player == "1":
            pawn_promotion_moves = []
            moves_to_delete = []
            for member in moves_list:
                if ("p" in member) and ("1" in member[5:6]):
                    moves_to_delete.append(member)
                    pawn_promotion_moves.append(member + "=n")
                    pawn_promotion_moves.append(member + "=b")
                    pawn_promotion_moves.append(member + "=r")
                    pawn_promotion_moves.append(member + "=q")
            if len(moves_to_delete) > 0:
                for member in moves_to_delete:
                    moves_list.remove(member)
            moves_list += pawn_promotion_moves
            return moves_list
            
    #update the board
    if operation == "update_board":
        #origin and destination of the piece
        origin = int(move[2:4])
        destination = int(move[5:7])
        new_piece = move[8:9]
        if origin < destination:
            first_limit = origin
            second_limit = destination
            updated_board = board[:first_limit] + "-" + board[first_limit + 1 : second_limit] + new_piece + board[second_limit + 1:100]
        else:
            first_limit = destination
            second_limit = origin
            updated_board = board[:first_limit] + new_piece + board[first_limit + 1 : second_limit] + "-" + board[second_limit + 1:100]
        return updated_board



#en passant operations
def en_passant(operation, status, move, board, player):
    #confirm if en passant is possible    
    if operation == "confirm":
        legality = False
        #return true if a pawn can capture on the en passant target square
        if ("P" in move) or ("p" in move):
            if (status == move[5:7]) and ("x" in move):           
                legality = True
        return legality
    #generate all en passant moves
    if operation == "generate_moves":
        #generate white moves
        if player == "0":
            moves = []
            #insert a black pawn inside the en passant target square
            board_list = list(board)
            board_list[int(status)] = "p"
            board = "".join(board_list)
            #create a list of pawn moves that will capture the inserted pawn
            square = 0    
            for i in board:
                if i == "P":  
                    moves = moves + white_pawn(square, board)
                square += 1
            en_passant_moves = []
            if len(moves) > 0:
                for member in moves:
                    if member[5:7] == status:
                        en_passant_moves.append(member)
            return en_passant_moves
        #generate black moves
        if player == "1":
            moves = []
            #insert a white pawn inside the en passant target square
            board_list = list(board)
            board_list[int(status)] = "P"
            board = "".join(board_list)
            #create a list of pawn moves that will capture the inserted pawn
            square = 0    
            for i in board:
                if i == "p":  
                    moves = moves + black_pawn(square, board)
                square += 1
            en_passant_moves = []
            if len(moves) > 0:
                for member in moves:
                    if member[5:7] == status:
                        en_passant_moves.append(member)
            return en_passant_moves
    #update the board
    if operation == "update_board":
        #origin and destination of the piece
        origin = int(move[2:4])
        destination = int(move[5:7])
        #determine the first and second limits, and update the board
        if origin < destination:
            first_limit = origin
            second_limit = destination
            updated_board = board[:first_limit] + "-" + board[first_limit + 1 : second_limit] + move[:1] + board[second_limit + 1:100]
            #replace the captured pawn's square with a hyphen
            board_list = list(updated_board)
            board_list[int(status) - 10] = "-"
            updated_board = "".join(board_list)
        else:
            first_limit = destination
            second_limit = origin
            updated_board = board[:first_limit] + move[:1] + board[first_limit + 1 : second_limit] + "-" + board[second_limit + 1:100]
            #replace the captured pawn's square with a hyphen
            board_list = list(updated_board)
            board_list[int(status) + 10] = "-"
            updated_board = "".join(board_list)
        return updated_board
                
            

#operations involving castling
def castling(operation, status, move, board, player):
    #update status
    if operation == "update_status":
        if ("O-O" in move) or ("O-O-O" in move):
            status = list(status)
            status[0] = 'F'
            status[1] = 'F'
        if ("o-o" in move) or ("o-o-o" in move):
            status = list(status)
            status[2] = 'F'
            status[3] = 'F'
        if ("K-15" in move):
            status = list(status)
            status[0] = 'F'
            status[1] = 'F'
        if ("k-85" in move):
            status = list(status)
            status[2] = 'F'
            status[3] = 'F'
        if ("R-11" in move):
            status = list(status)
            status[1] = 'F'
        if ("R-18" in move):
            status = list(status)
            status[0] = 'F'
        if ("r-81" in move):
            status = list(status)
            status[3] = 'F'
        if ("r-88" in move):
            status = list(status)
            status[2] = 'F'
        status = "".join(status)
        return status
    #generate moves
    if operation == "generate_moves":
        moves = []
        #white castling        
        if player == "0":
            if is_on_check(board, player) or (board[15] != "K"):
                return moves
            kingside_legality = True
            queenside_legality = True
            if (board[16] != "-") or (board[17] != "-") or (board[18] != "R"):
                kingside_legality = False      
            if (board[12] != "-") or (board[13] != "-") or (board[14] != "-") or (board[11] != "R"):
                queenside_legality = False 
            opponent = "1"
            possible_moves = moves_generator_rogue(board, opponent)
            for member in possible_moves:
                if ("16" in member) or ("17" in member):
                    kingside_legality = False
                    break
            if kingside_legality:
                moves.append("O-O")
            for member in possible_moves:
                if ("13" in member) or ("14" in member) or (board[22] == "p"):
                    queenside_legality = False
                    break
            if queenside_legality:
                moves.append("O-O-O")
        #black castling        
        if player == "1":
            if is_on_check(board, player) or (board[85] != "k"):
                return moves
            kingside_legality = True
            queenside_legality = True
            if (board[86] != "-") or (board[87] != "-") or (board[88] != "r"):
                kingside_legality = False      
            if (board[82] != "-") or (board[83] != "-") or (board[84] != "-") or (board[81] != "r"):
                queenside_legality = False 
            opponent = "0"
            possible_moves = moves_generator_rogue(board, opponent)
            for member in possible_moves:
                if ("86" in member) or ("87" in member):
                    kingside_legality = False
                    break
            if kingside_legality:
                moves.append("o-o")
            for member in possible_moves:
                if ("83" in member) or ("84" in member) or (board[72] == "P"):
                    queenside_legality = False
                    break
            if queenside_legality:
                moves.append("o-o-o")
        return moves 
    #update board
    if operation == "update_board":
        if move == "O-O":
            updated_board = board[:15] + "-" + board[15 + 1 : 17] + "K" + board[17 + 1:100]
            updated_board = updated_board[:16] + "R" + updated_board[16 + 1 : 18] + "-" + updated_board[18 + 1:100]
        if move == "O-O-O":
            updated_board = board[:11] + "-" + board[11 + 1 : 14] + "R" + board[14 + 1:100]
            updated_board = updated_board[:13] + "K" + updated_board[13 + 1 : 15] + "-" + updated_board[15 + 1:100]
        if move == "o-o":
            updated_board = board[:85] + "-" + board[85 + 1 : 87] + "k" + board[87 + 1:100]
            updated_board = updated_board[:86] + "r" + updated_board[86 + 1 : 88] + "-" + updated_board[88 + 1:100]
        if move == "o-o-o":
            updated_board = board[:81] + "-" + board[81 + 1 : 84] + "r" + board[84 + 1:100]
            updated_board = updated_board[:83] + "k" + updated_board[83 + 1 : 85] + "-" + updated_board[85 + 1:100]
        return updated_board
    #confirm if the castling move is allowed by the castling status flag
    if operation == "confirm":
        legality = False
        if status[0] == "K" and move == "O-O":
            legality = True
        if status[1] == "Q" and move == "O-O-O":
            legality = True
        if status[2] == "k" and move == "o-o":
            legality = True
        if status[3] == "q" and move == "o-o-o":
            legality = True
        return legality
 
 
        
#is the game a draw according to the board?
def is_on_draw(game, player):
    board = game[:100]
    game_status = game[100:].split('#')
    draw = True
    #find out if a player can play a legal move
    next_moves = []
    next_moves = moves_generator_rogue(board, player)
    next_moves += en_passant("generate_moves", game_status[8], False, board, player)
    next_moves = pawn_promotion("replace_moves", False, next_moves, False, player)
    if len(next_moves) == 0:
        draw = True
    else:
        for move in next_moves:
            if is_legal_move(game, move):
                draw = False
    #check for 50-move rule for a draw (100 moves for both players' moves)
    game_status = game[100:].split('#')
    moves_played = int(game_status[1])
    last_pawn_move = int(game_status[5])
    last_capture = int(game_status[6])
    if ((moves_played - last_pawn_move) > 99) and ((moves_played - last_capture) > 99):
        print "draw by 50-move rule"
        draw = True
    #check for 3-times repetition of a board position
    if len(game_status) > 9:
        past_positions = game_status[9]      
        gap = 0
        positions = []
        #transform the string (past_positions) into a list (positions)
        for i in range(len(past_positions) / 100):
            positions.append(past_positions[gap : gap + 100])
            gap += 100
        #check if a list member appears more than twice
        for member in positions:
            if positions.count(member) > 2:
                draw = True
                print "draw by repetition"
                break
    #calulate the mating-strength of either player
    mating_strength = False
    if (board.count("P") + board.count("p")) > 0:
        mating_strength = True
    elif (board.count("B") > 1) or (board.count("b") > 1):
        mating_strength = True
    elif (board.count("N") > 2) or (board.count("n") > 2):
        mating_strength = True
    elif (board.count("B") > 0) and (board.count("N")) > 0:
        mating_strength = True
    elif (board.count("b") > 0) and (board.count("n")) > 0:
        mating_strength = True
    elif (board.count("R") + board.count("r")) > 0:
        mating_strength = True
    elif (board.count("Q") + board.count("q")) > 0:
        mating_strength = True
    if mating_strength == False:
        print "draw due to insufficient mating strength"
        draw = True
    return draw



#is the player on checkmate according to the board?
def is_on_checkmate(game, player):
    board = game[:100]
    game_status = game[100:].split('#')
    check = False
    checkmate = True
    #identify if an opponent's move can capture the king
    if player == "0": #if the player is white
        king_position = str(board.find("K"))
        opponent = "1"
    if player == "1": #if the player is black
        king_position = str(board.find("k"))
        opponent = "0"        
    possible_moves = moves_generator_rogue(board, opponent)
    for member in possible_moves:
        if king_position in member:
            check = True
            break
    #find out if a player on check can escape check on the next move
    if check:
        next_moves = moves_generator_rogue(board, player)
        next_moves += en_passant("generate_moves", game_status[8], False, board, player)
        next_moves = pawn_promotion("replace_moves", False, next_moves, False, player)
        for move in next_moves:
            if is_legal_move(game, move):
                checkmate = False
    else:
        checkmate = False
    return checkmate



#returns true if the move played is legal
#first check the moves using moves_generator_rogue()
def is_legal_move(game, move):
    player = game[100]
    legality = True
    board = game[:100]
    #update the board
    #if it's a castling move, update the board
    game_status = game[100:].split('#')
    if (move == "O-O") or (move == "O-O-O") or (move == "o-o") or (move == "o-o-o") :
        updated_board = castling("update_board", False, move, board, False)
    #if it's an en passant move, update the board
    elif en_passant("confirm", game_status[8], move, False, False):
        updated_board = en_passant("update_board", game_status[8], move, board, False)
    #if it's a pawn promotion move, update the board
    elif pawn_promotion("confirm", move, False, False, False):
        updated_board =  pawn_promotion("update_board", move, False, board, False)
    else:     
        origin = int(move[2:4])
        destination = int(move[5:7])
        #determine the first and second limits, and update the board
        if origin < destination:
            first_limit = origin
            second_limit = destination
            updated_board = game[:first_limit] + "-" + game[first_limit + 1 : second_limit] + move[:1] + game[second_limit + 1:100]
        else:
            first_limit = destination
            second_limit = origin
            updated_board = game[:first_limit] + move[:1] + game[first_limit + 1 : second_limit] + "-" + game[second_limit + 1:100]
    #check if the current player has exposed a check
    check = False
    if player == "0":
        king_position = str(updated_board.find("K"))
        opponent = "1"
    if player == "1":
        king_position = str(updated_board.find("k"))
        opponent = "0"        
    possible_moves = moves_generator_rogue(updated_board, opponent)
    for member in possible_moves:
        if king_position in member:
            check = True
            break 
    if check == True:
        return False   
    return legality



#is the player on check according to the board?
def is_on_check(board, player):
    check = False 
    #identify if an opponent's move can capture the king
    if player == "0":
        king_position = str(board.find("K"))
        opponent = "1"
    if player == "1":
        king_position = str(board.find("k"))
        opponent = "0"        
    possible_moves = moves_generator_rogue(board, opponent)
    for member in possible_moves:
        if king_position in member:
            check = True
            break
    return check
        
        
        
#draws a chessboard using letters, dashes, and asterix
def draw_board(board):
    position = 90
    #10x10 board that includes an 8x8 chessboard within it
    for i in range(10):
        for i in range(10):
            print board[position],
            position += 1
        print
        position -= 20



#returns an updated game or returns the same game if the move played is illegal
def update_game_with_move(game, move):
    game_status = game[100:].split('#')
    number_of_moves_played = int(game_status[1])
    player = game[100]
    legality = False
    board = game[:100]
    #check if the game is on checkmate or draw
    if (game_status[3] == "1") or (game_status[4] == "1"):
        print "update_game_with_move()"
        print "check if the game is on checkmate or draw"
        return game
    #check if the move is in the list of possible moves
    possible_moves = moves_generator_rogue(board, player)
    possible_moves = pawn_promotion("replace_moves", False, possible_moves, False, player)
    for member in possible_moves:
            if move == member:
                legality = True    
    #castling moves
    if castling("confirm", game_status[7], move, False, False):
        for member in castling("generate_moves", False, False, board, player):
                if move == member:
                    legality = True
    #en passant moves
    if en_passant("confirm", game_status[8], move, False, False):
        for member in en_passant("generate_moves", game_status[8], False, board, player):
                if move == member:
                    legality = True
    #update the game
    if legality:
        #if it's a legal castling move, update the board
        if castling("confirm", game_status[7], move, False, False):            
           updated_board = castling("update_board", False, move, board, False)
        #if it's an en passant move, update the board
        elif en_passant("confirm", game_status[8], move, False, False):
            updated_board =  en_passant("update_board", game_status[8], move, board, False)   
        #if it's a pawn promotion move, update the board
        elif pawn_promotion("confirm", move, False, False, False):
            updated_board =  pawn_promotion("update_board", move, False, board, False)
        #update the board
        else:
            #origin and destination of the piece
            origin = int(move[2:4])
            destination = int(move[5:7])
            #determine the first and second limits, and update the board
            if origin < destination:
                first_limit = origin
                second_limit = destination
                updated_board = game[:first_limit] + "-" + game[first_limit + 1 : second_limit] + move[:1] + game[second_limit + 1:100]
            else:
                first_limit = destination
                second_limit = origin
                updated_board = game[:first_limit] + move[:1] + game[first_limit + 1 : second_limit] + "-" + game[second_limit + 1:100]
        #check if the current player has exposed a check due to an illegal move
        if is_on_check(updated_board, player):
            return game
        #player of the next move is updated
        if player == "0":
            player = "1"
        elif player == "1":
            player = "0"
        #check if the next player to move is on check
        check = '0'
        if is_on_check(updated_board, player):
            check = '1'
        #check if the next player to move is on checkmate or on draw
        checkmate = '0'
        draw = '0'
        #update the number of moves played
        number_of_moves_played += 1
        #update pawn moves
        pawn_move = game_status[5]
        if ("P" in move) or ('p' in move):
            pawn_move =  number_of_moves_played
        #update capture moves
        capture_move = game_status[6]
        if ("x" in move):
            capture_move =  number_of_moves_played
        #update castling availability
        castling_availability = game_status[7]
        if ("K" in move) or ("k" in move) or ("R" in move) or ("r" in move):
            castling_availability = castling("update_status", castling_availability, move, False, False)
        if ("O-O" in move) or ("O-O-O" in move) or ("o-o" in move) or ("o-o-o" in move):
            castling_availability = castling("update_status", castling_availability, move, False, False)
        #update en passant target square
        en_passant_target = "00"
        if "P" in move:
            if (int(move[5:7]) - int(move[2:4])) == 20:
                en_passant_target = int(move[2:4]) + 10
                en_passant_target = str(en_passant_target)
        if "p" in move:
            if (int(move[2:4]) - int(move[5:7])) == 20:
                en_passant_target = int(move[2:4]) - 10
                en_passant_target = str(en_passant_target)
        #update past board positions   
        past_positions = ""
        if len(game_status) > 9:
            past_positions = game_status[9]
        else:
            past_positions = game[:100]
        past_positions = past_positions + updated_board
        #update the game then return it
        new_game = updated_board + player + "#" + str(number_of_moves_played) + "#" + check + "#" + checkmate + "#" + draw + "#" + str(pawn_move) + "#" + str(capture_move) + "#" + castling_availability + "#" + en_passant_target + "#" + past_positions
        if is_on_checkmate(new_game, player):
            checkmate = '1'
            new_game = updated_board + player + "#" + str(number_of_moves_played) + "#" + check + "#" + checkmate + "#" + draw + "#" + str(pawn_move) + "#" + str(capture_move) + "#" + castling_availability + "#" + en_passant_target + "#" + past_positions
        if checkmate == '0':
            if is_on_draw(new_game, player):
                draw = '1'
                new_game = updated_board + player + "#"+ str(number_of_moves_played) + "#" + check + "#" + checkmate + "#" + draw + "#" + str(pawn_move) + "#" + str(capture_move) + "#" + castling_availability + "#" + en_passant_target + "#" + past_positions
        return new_game
    else:
        #if the move entered was illegal
        return game
         
    
     
#creates a list of all possible moves of all pieces
def moves_generator_rogue(board, player):
    moves = []
    #white moves
    if player == "0":
        #king moves
        square = 0
        for i in board:
            if i == "K":  
                moves = moves + white_king(square, board)
            square += 1 
        #queen moves
        square = 0
        for i in board:
            if i == "Q":  
                moves = moves + white_queen(square, board)
            square += 1
        #knight moves
        square = 0
        for i in board:
            if i == "N":  
                moves = moves + white_knight(square, board)
            square += 1 
        #pawn moves
        square = 0    
        for i in board:
            if i == "P":  
                moves = moves + white_pawn(square, board)
            square += 1
        #rook moves 
        square = 0
        for i in board:        
            if i == "R":  
                moves = moves + white_rook(square, board)
            square += 1
        #bishop moves 
        square = 0    
        for i in board:
            if i == "B":  
                moves = moves + white_bishop(square, board)
            square += 1 
    #black moves
    if player == "1":
        #king moves
        square = 0
        for i in board:
            if i == "k":  
                moves = moves + black_king(square, board)
            square += 1 
        #queen moves
        square = 0
        for i in board:
            if i == "q":  
                moves = moves + black_queen(square, board)
            square += 1
        #knight moves
        square = 0
        for i in board:
            if i == "n":  
                moves = moves + black_knight(square, board)
            square += 1 
        #pawn moves
        square = 0    
        for i in board:
            if i == "p":  
                moves = moves + black_pawn(square, board)
            square += 1
        #rook moves 
        square = 0
        for i in board:        
            if i == "r":  
                moves = moves + black_rook(square, board)
            square += 1
        #bishop moves 
        square = 0    
        for i in board:
            if i == "b":  
                moves = moves + black_bishop(square, board)
            square += 1
    #return a list of all possible moves of all pieces
    return moves



def custom_notation(game, move):
    """Convert a move to this software's custom notation from SAN (Standard
    Algebraic Notation) notation"""    
    
    move = move.upper()
    custom_move = move
    game_status = game[100:].split('#')
    number_of_moves_played = int(game_status[1])
    player = game[100]
    legality = False
    board = game[:100]
    
    #check if the game is on checkmate or draw
    if (game_status[3] == "1") or (game_status[4] == "1"):
        return "ERROR: Game is already on checkmate or draw"
        
    #check if the move is in the list of possible moves
    possible_moves = moves_generator_rogue(board, player)
    possible_moves = pawn_promotion("replace_moves", False, possible_moves, False, player)
    for member in  notation_dictionary(possible_moves).keys():
        if move[:len(member)] == member:
            custom_move =  notation_dictionary(possible_moves)[member]    

    #castling moves
    possible_moves = castling("generate_moves", False, False, board, player)
    for member in notation_dictionary(possible_moves).keys():
        if move[:len(member)] == member:
            if player == '1':
                custom_move = notation_dictionary(possible_moves)[member]
                custom_move = custom_move.lower()
            if player == '0':
                custom_move = notation_dictionary(possible_moves)[member]
    
    #en passant moves
    possible_moves = en_passant("generate_moves", game_status[8], False, board, player)
    for member in notation_dictionary(possible_moves).keys():
        if move[:len(member)] == member:
            custom_move = notation_dictionary(possible_moves)[member] 

    #update the game
    if player == 1:
        custom_move = custom_move.lower()    
    updated_game = update_game_with_move(game, custom_move)
    
    if updated_game == game:
        return "ERROR"
    else:
        return custom_move
        
        

def notation_dictionary(moves_list):
    """It takes a list of moves in custom notation and returns a dictionary
    The list ['P-25-45', 'N-17-36'] becomes {'E4': 'P-25-45', 'NF3': 'N-17-36'}
    """
    algebraic_moves = dict()
    long_to_algebraic = dict()
    long_to_algebraic['11'] = 'a1'
    long_to_algebraic['12'] = 'b1'
    long_to_algebraic['13'] = 'c1'
    long_to_algebraic['14'] = 'd1'
    long_to_algebraic['15'] = 'e1'
    long_to_algebraic['16'] = 'f1'
    long_to_algebraic['17'] = 'g1'
    long_to_algebraic['18'] = 'h1'
    long_to_algebraic['21'] = 'a2'
    long_to_algebraic['22'] = 'b2'
    long_to_algebraic['23'] = 'c2'
    long_to_algebraic['24'] = 'd2'
    long_to_algebraic['25'] = 'e2'
    long_to_algebraic['26'] = 'f2'
    long_to_algebraic['27'] = 'g2'
    long_to_algebraic['28'] = 'h2'
    long_to_algebraic['31'] = 'a3'
    long_to_algebraic['32'] = 'b3'
    long_to_algebraic['33'] = 'c3'
    long_to_algebraic['34'] = 'd3'
    long_to_algebraic['35'] = 'e3'
    long_to_algebraic['36'] = 'f3'
    long_to_algebraic['37'] = 'g3'
    long_to_algebraic['38'] = 'h3'
    long_to_algebraic['41'] = 'a4'
    long_to_algebraic['42'] = 'b4'
    long_to_algebraic['43'] = 'c4'
    long_to_algebraic['44'] = 'd4'
    long_to_algebraic['45'] = 'e4'    
    long_to_algebraic['46'] = 'f4'
    long_to_algebraic['47'] = 'g4'
    long_to_algebraic['48'] = 'h4'
    long_to_algebraic['51'] = 'a5' 
    long_to_algebraic['52'] = 'b5' 
    long_to_algebraic['53'] = 'c5' 
    long_to_algebraic['54'] = 'd5' 
    long_to_algebraic['55'] = 'e5' 
    long_to_algebraic['56'] = 'f5' 
    long_to_algebraic['57'] = 'g5' 
    long_to_algebraic['58'] = 'h5'
    long_to_algebraic['61'] = 'a6'
    long_to_algebraic['62'] = 'b6'
    long_to_algebraic['63'] = 'c6'
    long_to_algebraic['64'] = 'd6'
    long_to_algebraic['65'] = 'e6'
    long_to_algebraic['66'] = 'f6'
    long_to_algebraic['67'] = 'g6' 
    long_to_algebraic['68'] = 'h6'
    long_to_algebraic['71'] = 'a7'
    long_to_algebraic['72'] = 'b7'
    long_to_algebraic['73'] = 'c7'
    long_to_algebraic['74'] = 'd7'
    long_to_algebraic['75'] = 'e7'
    long_to_algebraic['76'] = 'f7'
    long_to_algebraic['77'] = 'g7'
    long_to_algebraic['78'] = 'h7'
    long_to_algebraic['81'] = 'a8' 
    long_to_algebraic['82'] = 'b8' 
    long_to_algebraic['83'] = 'c8' 
    long_to_algebraic['84'] = 'd8' 
    long_to_algebraic['85'] = 'e8' 
    long_to_algebraic['86'] = 'f8' 
    long_to_algebraic['87'] = 'g8' 
    long_to_algebraic['88'] = 'h8' 
    
    #create a dictionary for moves that share a destination
    #group together moves that have similar pieces going to same destination
    destinations = []
    for move in moves_list:
        if len(move) == 7:
            destinations.append(move[0] + move[5:7])
    repetitions = dict()
    for destin in destinations:
        repetitions[destin] = repetitions.get(destin, 0) + 1  # get returns value if key exists, otherwise 0.
    for member in repetitions.keys():
        if repetitions.get(member, 0) < 2:
            repetitions.pop(member)
    repetition_batches = []
    for destin in repetitions:
        repeated_batch = []
        for move in moves_list:        
            if (destin[0] == move[0]) and (destin[1:3] == move[5:7]):
                repeated_batch.append(move)
        repetition_batches.append(repeated_batch)
    
    #give a prefix showing unique origin of moves that have identical destinations
    prefix = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h'}
    for batch in repetition_batches:
        #how many pieces share the same rank and same file        
        rank_origins = []
        for move in batch:
            rank_origins.append(move[2])
        repetitions = dict()
        for origin in rank_origins:
            repetitions[origin] = repetitions.get(origin, 0) + 1  # get returns value if key exists, otherwise 0.
        for member in repetitions.keys():
            if repetitions.get(member, 0) < 2:
                repetitions.pop(member)
        rank_repetitions = repetitions        
        file_origins = []
        for move in batch:
            file_origins.append(move[3])
        repetitions = dict()
        for origin in file_origins:
            repetitions[origin] = repetitions.get(origin, 0) + 1  # get returns value if key exists, otherwise 0.
        for member in repetitions.keys():
            if repetitions.get(member, 0) < 2:
                repetitions.pop(member)
        file_repetitions = repetitions        
        
        if len(rank_repetitions) == 1 or len(file_repetitions) == 1:
            for member in batch:
                #if two pieces' origins have the same rank
                move = member.upper()
                if rank_repetitions.get(move[2]) == 2 and file_repetitions.get(move[3], 0) == 0:                
                    if move[4] == '-':
                        algeb_move = move[:1] + prefix[move[3]] + long_to_algebraic[move[5:7]] + move[7:]
                        algebraic_moves[algeb_move] = member
                        moves_list.remove(member) 
                    if move[4] == 'X':
                        algeb_move = move[:1]  + prefix[move[3]] + 'X' + long_to_algebraic[move[5:7]] + move[7:]
                        algebraic_moves[algeb_move] = member
                        moves_list.remove(member) 
                #if two pieces' origins have the same file
                if file_repetitions.get(move[3]) == 2 and rank_repetitions.get(move[2], 0) == 0:
                    if move[4] == '-':
                        algeb_move = move[:1] + move[2] + long_to_algebraic[move[5:7]] + move[7:]
                        algebraic_moves[algeb_move] = member
                        moves_list.remove(member) 
                    if move[4] == 'X':
                        algeb_move = move[:1]  + move[2] + 'X' + long_to_algebraic[move[5:7]] + move[7:]
                        algebraic_moves[algeb_move] = member
                        moves_list.remove(member)
                #if one piece's origin shares both a file and a rank with other pieces
                if rank_repetitions.get(move[2], 0) > 1 and file_repetitions.get(move[3], 0) > 1:
                    algeb_move = long_to_algebraic[move[2:4]] + long_to_algebraic[move[5:7]] + move[7:]
                    algebraic_moves[algeb_move] = member
                    moves_list.remove(member)
                    
    #create a dictionary for moves that don't share one destination
    for member in moves_list:
        move = member.upper()
        if (move == 'O-O-O') or (move == 'O-O'):
            algebraic_moves[move.upper()] = member
        else:         
            if move[4] == '-':
                if move[0] == 'P':
                    algeb_move = long_to_algebraic[move[5:7]] + move[7:]
                    algebraic_moves[algeb_move.upper()] = member    
                else:
                    algeb_move = move[:1] + long_to_algebraic[move[5:7]] + move[7:]
                    algebraic_moves[algeb_move.upper()] = member
            if move[4] == 'X':
                if move[0] == 'P':
                    pawn_origin = long_to_algebraic[move[2:4]][0]
                    algeb_move = pawn_origin + 'X' + long_to_algebraic[move[5:7]] + move[7:]
                    algebraic_moves[algeb_move.upper()] = member
                else:
                    algeb_move = move[:1] + 'X' + long_to_algebraic[move[5:7]] + move[7:]
                    algebraic_moves[algeb_move.upper()] = member
    return algebraic_moves                          



#evaluate who is winning a game
def evaluate_game(game):
    board = game[:100]
    piece_values = dict()
    piece_values['K'] = 100
    piece_values['Q'] = 9
    piece_values['R'] = 5
    piece_values['B'] = 3
    piece_values['N'] = 3
    piece_values['P'] = 1
    piece_values['k'] = -100
    piece_values['q'] = -9
    piece_values['b'] = -5
    piece_values['n'] = -3
    piece_values['r'] = -3
    piece_values['p'] = -1
    piece_values['*'] = 0
    piece_values['-'] = 0
    game_value = 0
    for char in board:
        game_value += piece_values[char]        
    return game_value


#evaluate the value of each move from a list of moves
def evaluate_moves(moves_list, game):
    move_values = dict()
    for move in moves_list:
        updated_game = update_game_with_move(game, move)
        move_values[move] = evaluate_game(updated_game)
    return move_values
    

#choose a move from a dictionary of moves
def engine_player(game):
    player = game[100]
    game_status = game[100:].split('#')
    possible_moves = moves_generator_rogue(game[:100], player)
    possible_moves += castling("generate_moves", False, False, game[:100], player)
    possible_moves += en_passant("generate_moves", game_status[8], False, game[:100], player)
    possible_moves = pawn_promotion("replace_moves", False, possible_moves, False, player)
    legal_moves = []
    for move in possible_moves:
        if is_legal_move(game, move):
            legal_moves.append(move)
    if player == "0" and len(legal_moves) != 0:
        move_values = evaluate_moves(legal_moves, game)
        best_move = legal_moves[0]
        print "engine_player's first legal move:", best_move
        for move in move_values:
            if move_values[move] > move_values[best_move]:
                best_move = move
        print "engine_player's move:", best_move
        updated_game = update_game_with_move(game, best_move)
        return updated_game 
    if player == "1" and len(legal_moves) != 0:
        move_values = evaluate_moves(legal_moves, game)
        best_move = legal_moves[0]
        print "engine_player's first legal move:", best_move
        for move in move_values:
            if move_values[move] < move_values[best_move]:
                best_move = move
        print "engine_player's move:", best_move              
        updated_game = update_game_with_move(game, best_move)
        return updated_game
    else:
        return "engine_player has no legal move"    


#automatically playing moves randomly
def engine_random_move(game):
    player = game[100]
    game_status = game[100:].split('#')
    possible_moves = moves_generator_rogue(game[:100], player)
    possible_moves += castling("generate_moves", False, False, game[:100], player)
    possible_moves += en_passant("generate_moves", game_status[8], False, game[:100], player)
    possible_moves = pawn_promotion("replace_moves", False, possible_moves, False, player)
    legal_moves = []
    for move in possible_moves:
        if is_legal_move(game, move):
            legal_moves.append(move)
    if len(legal_moves ) != 0:
        move = random.choice(legal_moves)
        updated_game = update_game_with_move(game, move)
        print "engine_random_move: ", move
        return updated_game
    else:
        return "engine_random has no legal move"
                    


def random_vs_selective_engine():
    """random-based engine versus selective engine"""    
    game = new_game()    
    #game that lasts a maximum of 200 moves (400 plys)
    for i in range(200):
        game = engine_random_move(game)
        if game != "engine_random has no legal move":
            print
            draw_board(game[:100])
            print game[:130]
            player = game[100]
            if is_on_draw(game, player):
                break
            if is_on_checkmate(game, player):
                break
        game = engine_player(game)
        if game != "engine_player has no legal move":
            print
            draw_board(game[:100])
            print game[:130]
            player = game[100]
            if is_on_draw(game, player):
                break
            if is_on_checkmate(game, player):
                break
    print "Game over"



def selective_vs_selective_engine():
    """selective engine versus selective engine"""    
    game = new_game()    
    #game that lasts a maximum of 200 moves (400 plys)
    for i in range(200):
        game = engine_player(game)
        if game != "engine_random has no legal move":
            print
            draw_board(game[:100])
            print game[:130]
            player = game[100]
            if is_on_draw(game, player):
                break
            if is_on_checkmate(game, player):
                break
        game = engine_player(game)
        if game != "engine_player has no legal move":
            print
            draw_board(game[:100])
            print game[:130]
            player = game[100]
            if is_on_draw(game, player):
                break
            if is_on_checkmate(game, player):
                break
    print "Game over"



def random_vs_random_engine():
    """random-based engine versus selective engine"""    
    game = new_game()    
    #game that lasts a maximum of 200 moves (400 plys)
    for i in range(200):
        game = engine_random_move(game)
        if game != "engine_random has no legal move":
            print
            draw_board(game[:100])
            print game[:130]
            player = game[100]
            if is_on_draw(game, player):
                break
            if is_on_checkmate(game, player):
                break
        game = engine_random_move(game)
        if game != "engine_player has no legal move":
            print
            draw_board(game[:100])
            print game[:130]
            player = game[100]
            if is_on_draw(game, player):
                break
            if is_on_checkmate(game, player):
                break
    print "Game over"



def human_vs_human():
    game = new_game()
    keyboard_entry = ""
    while keyboard_entry != "quit":
        print "\n\n"
        draw_board(game[:100])
        print "\n"       
        print "Enter your move:"
        keyboard_entry = raw_input()
        #convert from SAN notation to the custom notation
        move = custom_notation(game, keyboard_entry)
        #update the game using the entered move
        updated_game = update_game_with_move(game, move)
        if game != updated_game:
            game = updated_game
            #check if the game has ended due to a checkmate or a draw
            game_status = game[100:].split('#')
            if game_status[3] == "1":
                draw_board(game[:100]) 
                print "Checkmate! The winner of the game is:",
                if game_status[0] == "0":
                    print "Black"
                if game_status[0] == "1":
                    print "White"
                break
            if game_status[4] == "1":
                draw_board(game[:100])
                print "Draw! The game has ended in a draw"
                break
        else:
            print "Your move (",keyboard_entry,") was illegal"
    print "Game over."
    


def human_vs_computer_1():
    game = new_game()
    keyboard_entry = ""
    while keyboard_entry != "quit":
        print "\n\n"
        draw_board(game[:100])
        print "\n"        
        keyboard_entry = raw_input("Enter your move: ")
        #convert from SAN notation to the custom notation
        move = custom_notation(game, keyboard_entry)
        #update the game
        updated_game = update_game_with_move(game, move)
        if game != updated_game:
            game = updated_game
            game_status = game[100:].split('#')
            if game_status[3] == "1":
                draw_board(game[:100])
                print "Checkmate! The winner of the game is:",
                if game_status[0] == "0":
                    print "Black"
                if game_status[0] == "1":
                    print "White"
                break
            if game_status[4] == "1":
                draw_board(game[:100])
                print "Draw! The game has ended in a draw"
                break
            game = engine_random_move(game)
            game_status = game[100:].split('#')
            if game_status[3] == "1":
                draw_board(game[:100])
                print "Checkmate! The winner of the game is:",
                if game_status[0] == "0":
                    print "Black"
                if game_status[0] == "1":
                    print "White"
                break
            if game_status[4] == "1":
                draw_board(game[:100])
                print "Draw! The game has ended in a draw"
                break
        else:
            print "Your move (",keyboard_entry, ") was illegal"
    print "Game over."    
    


def human_vs_computer_2():
    game = new_game()
    keyboard_entry = ""
    while keyboard_entry != "quit":
        print "\n\n"
        draw_board(game[:100])
        print "\n"
        keyboard_entry = raw_input("Enter your move: ")
        #convert from SAN notation to the custom notation
        move = custom_notation(game, keyboard_entry)
        #update the game
        updated_game = update_game_with_move(game, move)
        if game != updated_game:
            game = updated_game
            game_status = game[100:].split('#')
            if game_status[3] == "1":
                draw_board(game[:100])
                print "Checkmate! The winner of the game is:",
                if game_status[0] == "0":
                    print "Black"
                if game_status[0] == "1":
                    print "White"
                break
            if game_status[4] == "1":
                draw_board(game[:100])
                print "Draw! The game has ended in a draw"
                break
            #game = engine_random_move(game)
            game = engine_player(game)
            game_status = game[100:].split('#')
            if game_status[3] == "1":
                draw_board(game[:100])
                print "Checkmate! The winner of the game is:",
                if game_status[0] == "0":
                    print "Black"
                if game_status[0] == "1":
                    print "White"
                break
            if game_status[4] == "1":
                draw_board(game[:100])
                print "Draw! The game has ended in a draw"
                break
        else:
            print "Your move (",keyboard_entry,") was illegal"
    print "Game over."


    
def menu():
    print "\n\n"
    print "Choose an option:"
    print "    1: Human vs Computer (Level 1)"
    print "    2: Human vs Computer (Level 2)"
    print "    3: Human vs Human - Play against another person"
    print "    4: Computer vs Computer - Level 1 vs Level 2"
    print "    5: Computer vs Computer - Level 2 vs Level 2"
    print "    6: Computer vs Computer - Level 1 vs Level 1"
    print "    7: Exit."
    
    keyboard_input = raw_input()    
    if keyboard_input == '1':
        human_vs_computer_1()
        print "\n\n"
        return True    
    if keyboard_input == '2':
        human_vs_computer_2()
        print "\n\n"
        return True
    if keyboard_input == '3':
        human_vs_human()
        print "\n\n"
        return True     
    if keyboard_input == '4':
        random_vs_selective_engine()
        print "\n\n"
        return True 
    if keyboard_input == '5':
        selective_vs_selective_engine()
        print "\n\n"
        return True 
    if keyboard_input == '6':
        random_vs_random_engine()
        print "\n\n"
        return True 
    if keyboard_input == '7':
        return False
    return True
                   

    
if __name__ == '__main__':
    execute = True
    while execute:
        execute = menu()
