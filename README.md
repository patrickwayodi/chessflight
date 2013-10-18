chessflight
===========

Chessflight is software for playing chess. It can be used for human versus computer play, human versus human play, and computer versus computer play. The program plays at two levels of difficulty: Level 1 plays random (but legal) moves while Level 2 is slightly stronger. It is written in Python.

These are installation instructions for this software:
Step 1: Install Python if you do not already have it
Step 2: Run the file named chessriver.py
Step 3: Choose one of the options


The program has these four majour components: chess logic, chess engine, notation conversion, and a user interface.

The chess board has 64 squares but this software uses additional squares to
represent the border of the chess board, making a total of 100 squares (numbered
0 to 99) as shown below. The chess board itself has squares numbered from 11 to 88, with the border
squares skipped.

The programtakes a move and a game's state as inputs and then returning
an updated game (or returning the same game if the move was illegal). The
function play_move(game, move) takes two arguments: a move that is in the form
of Standard Algebraic Notation and a string that represents the current state of
the game. It first converts the move into the project's custom notation and then
it updates the game by calling the function update_game_with_move(game, move)
which returns an updated game or returns the same game if the move played is
illegal.

To generate all the possible moves for a chess board position, the function
moves_generator_rogue(board, player) is used. It accepts two arguments: a string
representing a chess board position, and an interger (0 or 1)representing the
player whose turn it is to play. And then it returns a list of all the possible
moves that can be played by all the chess pieces of tha player.

Each chess piece (king, queen, rook, bishop, knight, and pawn) has a python
function that generates all the moves that it could possibly play in a certain
chess board position. Since there are separate functions for white and black
pieces, there are a total of 12 functions for the chess pieces. These functions
accept two arguments - the square at which the piece is located (an integer) and
the current state of the chess board - and then return a list of all the
possible moves that could be played by the piece.


CREDITS:
The principal author of this project is me, Patrick Wayodi
<patrickwayodi@yahoo.com>. I am grateful to the following people who have
contributed source code, documentation, or ideas to this project:
    Ambrose Olwa
    Joseph Wayodi


LICENSE:
This software is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. See the GNU General Public License for more details. You should have
received a copy of the GNU General Public License along with this software.  If
not, see http://www.gnu.org/licenses/

This software is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.
