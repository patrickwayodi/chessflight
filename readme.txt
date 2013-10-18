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

Appendix A - Standard Algebraic Notation
Appendix B - Custom Chess Notation
Glossary
References
Index



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
0 to 99) as shown below:

90  91 92 93 94 95 96 97 98  99
   ------------------------- 
80 |81|82|83|84|85|86|87|88| 89
   -------------------------
70 |71|72|73|74|75|76|77|78| 79
   -------------------------
60 |61|62|63|64|65|66|67|68| 69
   -------------------------
50 |51|52|53|54|55|56|57|58| 59
   -------------------------
40 |41|42|43|44|45|46|47|48| 49
   -------------------------
30 |31|32|33|34|35|36|37|38| 39
   -------------------------
20 |21|22|23|24|25|26|27|28| 29
   ---------------------
10 |11|12|13|14|15|16|17|18| 19
   -------------------------
 0   1  2  3  4  5  6  7  8   9


The chess board itself has squares numbered from 11 to 88, with the border
squares skipped:

|81|82|83|84|85|86|87|88|
-------------------------
|71|72|73|74|75|76|77|78|
-------------------------
|61|62|63|64|65|66|67|68|
-------------------------
|51|52|53|54|55|56|57|58|
-------------------------
|41|42|43|44|45|46|47|48|
-------------------------
|31|32|33|34|35|36|37|38|
-------------------------
|21|22|23|24|25|26|27|28|
-------------------------
|11|12|13|14|15|16|17|18|



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

This will be the future drawn board for the command line user interface:           
    r n b q k b n r
    p p p p p p p p
    . . . . . . . .
    . . . . . . . .
    . . . . . . . .
    . . . . . . . .
    P P P P P P P P
    R N B Q K B N R

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
    
Version 0.6.9
    Source code for playing chess combined into the file "chessriver.py"
    Source code that doesn't deal with playing chess is deleted

Version 0.6.8
    added more documentation

Version 0.6.7
    modified documentation
        "todo" file deleted, with some parts going to "hacking" and "ideas"
     
Version 0.6.6
    removed obsolete code from the module chess.py
    added documentation
    renamed all developer-only support files to "xx.*" (xx.py, xx.png, xx.txt)    

Version 0.6.5
    starting of a tournament round
        pairing of the players
        inserting a 'new_game' as a first move to serve as a reference
    modified a tournament's objects
        added 'result' to 'games'
        added 'points' to 'tournament_players'
        added 'playing_strength' to 'users'
        added 'round' to 'games'

Version 0.6.4
    password authentication
    registering to participate in tournaments
    
Version 0.6.3
    registering a new user
    creating a new tournament

Version 0.6.2    
    increased options in playing against the computer:
        two levels of strength introduced (random-based or single-depth search)
    re-introduced playing of moves using SAN (Standard Algebraic Notation)
        notation.py translates SAN notation to custom notation

Version 0.6.1
    engine code modified for playing various "engine versus engine" permutations
    user interface introduced for "engine versus engine" play
    most modules have been given a user interface
        user.py has been phased off

Version 0.6.0
    re-introduced conversion of SAN notation to the custom notation
        custom_notation(game, move)
        test_custom_notation()
    playing against the computer using SAN notation

Version 0.5.9
    re-organized the code for the user interface and for tournaments
        play_against_computer() is now part of tournament.py
    play against the computer now uses the software's custom notation, not SAN
        SAN (Standard Algebraic Notation) is being implemented separately
    created a photo with numbered squares to help when using the custom notation

Version 0.5.8
    added tests for draw by stalemate and draw by repetition
    added experiments to make chess board code more readable
    improved the documentation

Version 0.5.7
    completed the test for play_move()
        test_play_move_newgame()
    renamed the module usercli.py to user.py
    improved the documentation
        hacking.txt

Version 0.5.6
    improved documentation

Version 0.5.5
    tests for the source code
    improved documentation    

Version 0.5.4
    changed the name of the project from "chessix" to "chess"
    re-organized and re-wrote the documentation to make it collaboration-ready

0.5.3
    additional engine that evalutes only one-step deep using piece values    

0.5.2
    user interface for playing against the engine using algebraic notation 
    
0.5.1 algebraic notation fully implemented

0.5.0 algebraic notation partially implemented

0.4.9 pawn promotion

0.4.8 en passant fully implemented

0.4.7 en passant partially implemented

0.4.6 added castling ability

0.4.5 draw due to insufficient mating-strength, added castling availability

0.4.4 added the rule for draw by 3-times repetition of a board position

0.4.3 added the 50-move rule for a draw

0.4.2 added two engines, combined the admin and command-line files

0.4.1 updating the game for a draw when the king is trapped but not on check

0.4.0 updating the game state for a checkmate condition

Version 0.3.9 rejecting illegal moves that expose the player to check

Version 0.3.8 updating the game state for a check condition

Version 0.3.7 added some documentation

Version 0.3.6 creating a tournament and beginning a tournament, but still incomplete

Version 0.3.5 pairing of players and their opponents in a tournament

Version 0.3.4 split into back-end and front ends, and command-line front-end added

Version 0.3.3 further design of a tournament in the documentation

Version 0.3.2
    database modifications and designing of a tournament in the documentation

Version 0.3.1
    playing using messages from the inputs database, but very buggy

Version 0.3.0
    creating a new game for registered players

Version 0.2.9
    added some documentation

Version 0.2.8 registering of players using messages they sent

Version 0.2.7 added an extra database, and the use of arguments in the sql code

Version 0.2.6 added modules and a main source file

Version 0.2.5 added databases

Version 0.2.4
    identifies if a player is on check
    
0.2.3 counting of moves, and working with game-status flags

0.2.2 documentation updated

0.2.1 chess engine that plays chess against itself using random moves

0.2.0 simplified the code to ease future re-factoring

0.1.9 tested with different moves-lists, and bugs removed

0.1.8 some bugs removed, but major bugs still left

0.1.7 automatically reading moves played from a list, and de-bugging

Version 0.1.6 legality of moves checked, and turn-based gaming introduced

Version 0.1.5 black pieces added, and source code simplified

Version 0.1.4 added king, queen, knight, and gpl v2 license to source file

Version 0.1.3 8x8 chessboard with pawn, rook, and bishop moves only

Version 0.1.2 more documentation added to the source code

Version 0.1.1
    documentation added to the source code

Version 0.1.0
    queen moves added

Version 0.0.9
    addition of all knight moves

Version 0.0.8
    bishop moves, and knight moves that have several bugs

Version 0.0.7
    all rook moves

Version 0.0.6
    forward-marching, backward-marching and capturing rook

Version 0.0.5
    forward-marching rook, but bugs with the backward-marching part

Version 0.0.4
    generates captures and special moves of pawn, except en-passant

Version 0.0.3
    generates one special pawn move in adddition to other pawn moves

Version 0.0.2
    generates some pawn moves, but no special moves

Version 0.0.1
    draws a chess board from a string input



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
