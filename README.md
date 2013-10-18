chessflight
===========

Chessflight is software for playing chess. It can be used for human versus computer play, human versus human play, and computer versus computer play. The program plays at two levels of difficulty: Level 1 plays random (but legal) moves while Level 2 is slightly stronger. It is written in Python.

TABLE OF CONTENTS

1. Installation and Use
2. Hacking
    2.1 Chess board
    2.2 Python functions
    2.3 Updating a chess game
    2.4 Generating all possible moves
    2.5 Chess pieces
3. Future Plans
4. Version History
5. Bugs
    5.1 Adjudication of draws due to repetition may be faulty
    5.2 The program crashes after a checkmating move (Qh5) is made
    5.3 The program crashes after a checkmating move (Qxf7) is made
6. Credits
7. License



1. INSTALLATION AND USE

These are installation instructions for this software:
    Step 1: Install Python if you do not already have it
    Step 2: Run the file named chessriver.py
    Step 3: Choose one of the options by entering a digit between 1 and 7:
                Human vs Computer (Level 1)
                Human vs Computer (Level 2)
                Human vs Human - Play against another person
                Computer vs Computer - Level 1 vs Level 2
                Computer vs Computer - Level 2 vs Level 2
                Computer vs Computer - Level 1 vs Level 1
                Exit



2. HACKING

The program has these four majour components:
    chess logic
    chess engine
    notation conversion
    user interface



2.1 CHESS BOARD

The chess board has 64 squares but this software uses additional squares to
represent the border of the chess board, making a total of 100 squares (numbered
0 to 99) as shown below. The chess board itself has squares numbered from 11 to 88, with the border
squares skipped.



2.2 PYTHON FUNCTIONS

The program has the following Python functions:
    new_game()
    white_king(square, board)
    white_queen(square, board)
    white_knight(square, board)
    white_pawn(square, board)
    white_rook(square, board)
    white_bishop(square, board)
    black_king(square, board)
    black_queen(square, board)
    black_knight(square, board)
    black_pawn(square, board)
    black_rook(square, board)
    black_bishop(square, board)
    pawn_promotion(operation, move, moves_list, board, player)
    en_passant(operation, status, move, board, player)
    castling(operation, status, move, board, player)
    is_on_draw(game, player)
    is_on_checkmate(game, player)
    is_legal_move(game, move)
    is_on_check(board, player)
    draw_board(board)
    update_game_with_move(game, move)
    moves_generator_rogue(board, player)
    custom_notation(game, move)
    notation_dictionary(moves_list)
    evaluate_game(game)
    evaluate_moves(moves_list, game)
    engine_player(game)
    engine_random_move(game)
    random_vs_selective_engine()
    selective_vs_selective_engine()
    random_vs_random_engine()
    human_vs_human()
    human_vs_computer_1()
    human_vs_computer_2()
    menu()



2.3 UPDATING A CHESS GAME

The module chess.py takes a move and a game's state as inputs and then returning
an updated game (or returning the same game if the move was illegal). The
function play_move(game, move) takes two arguments: a move that is in the form
of Standard Algebraic Notation and a string that represents the current state of
the game. It first converts the move into the project's custom notation and then
it updates the game by calling the function update_game_with_move(game, move)
which returns an updated game or returns the same game if the move played is
illegal.

A game state's notation (e.g. ...***1#97#0#0#1#83#86#FFFF#00#***...)
    *board (string) 
    *player to play (0-white/1-black)
    *number of moves played (integer)
    *check (0-False/1-True) 
    *checkmate (0-False/1-True)
    *draw (0-False/1-True)
    *last move number for a pawn move (integer)
    *last move number for a capture (integer)
    *castling availability (0-False/KQkq-True/KQk0/KQ0q/e.t.c./e.t.c.)
    *en passant target square(behind any pawn that's just moved 2-squares)
    *past positions combined with current position    
Note that a new game's state doesn't include a hash(#) at the end.



2.4 GENERATING ALL POSSIBLE MOVES

To generate all the possible moves for a chess board position, the function
moves_generator_rogue(board, player) is used. It accepts two arguments: a string
representing a chess board position, and an interger (0 or 1)representing the
player whose turn it is to play. And then it returns a list of all the possible
moves that can be played by all the chess pieces of tha player.



2.5 CHESS PIECES

Each chess piece (king, queen, rook, bishop, knight, and pawn) has a python
function that generates all the moves that it could possibly play in a certain
chess board position. Since there are separate functions for white and black
pieces, there are a total of 12 functions for the chess pieces. These functions
accept two arguments - the square at which the piece is located (an integer) and
the current state of the chess board - and then return a list of all the
possible moves that could be played by the piece.



3. FUTURE PLANS

These are some program features that are planned for the future:
(a) A single python function that controls engine vs. engine play instead of
    having several functions.
(b) Additional user interfaces like web and GUI.
(c) Storing of the games in a database.
(d) A log file

Future implementation of tests could include a brute force chess player
    [letter]+[letter]+[number]-or-[o-o-o]-or[0-0]or[e.t.c.]
    both black and white moves alternatingly
    tries millions of both legal and illegal moves
    creates a log of the games played that contains the accepted moves
    
Future testing of algebraic inputs:
    integer-castling (0-0 instead of O-O and o-o)
        parse a pgn file
            pgn.py
            put highlights in another file
        moves of identical pieces to the same square
            e.g. N1f4 and N4xf4 and c4b6
        lowercase moves
        uppercase moves
        black castling
        
The program will have a website interface.

The program will also have a database interface:
    export and import of pgn files
    hack it with the help of the "SQLite database browser"
    implement an orm (object relational model) for the database
    a program that splits the "million chess database" into individual files
        /appsyodi/chess/pgn.py

The tests for the chess code are in the file "tests.py"

The ability to organize tournaments will be added:
    register a new player
    create a new tournament
    register to participate in a tournament
    start a tournament round
    play a move in a tournament game



4. VERSION HISTORY

Version 0.7.3
    Documentation added
    License updated to version 3 (from version 2) of GNU GPL

Version 0.7.2
    Source file re-named to "chessflight.py"
    Version numbering to include version numbers of earlier chess app

Version 0.7.1
    Command line interface made to be more user friendly
    Documentation added

Version 0.7.0
    Documentation combined into a single file, "readme.txt"
    Start menu editted
5. BUGS

Each submitted bug report should have these fields:
    Title
    Summary
    Status
    Error Message
    Comments
    System Details



5.1 ADJUDICATION OF DRAWS DUE TO REPETITION MAY BE FAULTY

SUMMARY:
In the game's state, the section with past positions also includes the current
position. This could affect the software's ability to adjudicate draws due to
repetition.

STATUS:
Resolved
It isn't a bug; the draw adjudication works fine

ERROR MESSAGE:
none

COMMENTS:
A test should be written for the software's ability to adjudicate draws due to
repetition.

SYSTEM DETAILS:
debain gnu/linux 6.0
hp pavilion dv6



5.2 THE PROGRAM CRASHES AFTER A CHECKMATING MOVE (QH5) IS MADE

STATUS:
Resolved
The problem was that the user interface code wasn't properly checking for
checkmate

ERROR MESSAGE:
Traceback (most recent call last):
  File "usercli.py", line 93, in <module>
    menu()
  File "usercli.py", line 17, in menu
    play_against_computer()    
  File "usercli.py", line 39, in play_against_computer
    if game_status[3] == "1":
IndexError: list index out of range

COMMENTS:
the bug has been repeated once

SYSTEM DETAILS:
debain gnu/linux 6.0
hp pavilion dv6



5.3 THE PROGRAM CRASHES AFTER A CHECKMATING MOVE (QXF7) IS MADE

STATUS:
Resolved
The problem was that the user interface code wasn't properly checking for
checkmate

ERROR MESSAGE:
Traceback (most recent call last):
  File "usercli.py", line 93, in <module>
    menu()
  File "usercli.py", line 17, in menu
    play_against_computer()    
  File "usercli.py", line 39, in play_against_computer
    if game_status[3] == "1":
IndexError: list index out of range

COMMENTS:
the bug hasn't been repeated yet

SYSTEM DETAILS:
debain gnu/linux 6.0
hp pavilion dv6



6. CREDITS

The principal author of this project is me, Patrick Wayodi
<patrickwayodi@yahoo.com>. I am grateful to the following people who have
contributed source code, documentation, or ideas to this project:
    Ambrose Olwa
    Joseph Wayodi



7. LICENSE

This software is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. See the GNU General Public License for more details. You should have
received a copy of the GNU General Public License along with this software.  If
not, see http://www.gnu.org/licenses/

This software is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.
