# Tic-Tac-Toe
# For Dari's Texton App
# Author Jaween Ediriweera
# Date 2024-03-13

from enum import Enum
import os
import random
import time

# This can be replaced with Texton's clear() function when integrated.
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Piece(Enum):
    Naught = 0
    Cross = 1

class Player(Enum):
    Human = 0
    Computer = 1

def piece_to_string(piece: Piece) -> str:
    if piece is None:
        return " "
    return "O" if piece is Piece.Naught else "X"

def board_to_string(board: list[Piece]) -> str:
    buffer = ""
    buffer = buffer + "    1  2  3"
    for y in range(3):
        buffer = buffer + f"\n{y + 1} |"
        for x in range(3):
            buffer = buffer + f" {piece_to_string(board[index_of(x, y)])} "
        buffer = buffer + "|"
    return buffer

def index_of(x: int, y: int) -> int:
    return y * 3 + x

def is_in_bounds(x: int, y: int) -> bool:
    if x < 0 or x >= 3 or y < 0 or y >= 3:
        return False
    return True

def is_space_free(board: list[Piece], x: int, y: int) -> bool:
    return board[index_of(x, y)] is None

def get_players() -> dict[Piece, Player]:
    mode = -1
    while mode < 0 or mode > 3:
        clear()
        print("Welcome to Tic-Tac-Toe!\n")
        print("Choose game mode:")
        print(' [1] Human Vs. Computer')
        print(' [2] Human Vs. Human')
        print(' [3] Computer Vs. Computer\n')
        result = input("")
        try:
            mode = int(result.strip().replace("[", "").replace("]", ""))
        except:
            mode = -1
            continue
    
    pieces = [Piece.Naught, Piece.Cross]
    random.shuffle(pieces)
    return {
        pieces[0]: Player.Human if mode == 1 or mode == 2 else Player.Computer,
        pieces[1]: Player.Human if mode == 2 else Player.Computer,
    }

def get_human_input(piece: Piece) -> tuple[int, int]:
    line = input(f"\n{piece_to_string(piece)}'s turn: ")
    tokens = line.strip(" ").split(" ")
    try:
        return (int(tokens[1]) - 1, int(tokens[0]) - 1)
    except:
        return (None, None)

def get_computer_input(piece: Piece, board: list[Piece]) -> tuple[int, int]:
    print(f"\n{piece_to_string(piece)}'s turn, computer is thinking...")
    time.sleep(1)
    while True:
        x = random.randrange(3)
        y = random.randrange(3)
        if is_space_free(board, x, y):
            return (x, y)

def display_header(board: list[Piece]) -> None:
    clear()
    print(f"  Tic-Tac-Toe\n")
    print(board_to_string(board),)

def display_end_screen(board: list[Piece], winner: Piece) -> None:
    display_header(board)
    print("")
    if winner is None:
        print("     Draw!")
    else:
        print(f"    {piece_to_string(winner)} wins!")

def find_winner(board: list[Piece]) -> Piece:
    # Check rows
    for y in range(3):
        piece0 = board[index_of(0, y)]
        piece1 = board[index_of(1, y)]
        piece2 = board[index_of(2, y)]
        if piece0 is not None and piece0 is piece1 and piece1 is piece2:
            return piece0

    # Check columns
    for x in range(3):
        piece0 = board[index_of(x, 0)]
        piece1 = board[index_of(x, 1)]
        piece2 = board[index_of(x, 2)]
        if piece0 is not None and piece0 is piece1 and piece1 is piece2:
            return piece0

    # Check both diagonals
    piece0 = board[index_of(0, 0)]
    piece1 = board[index_of(1, 1)]
    piece2 = board[index_of(2, 2)]
    if piece0 is not None and piece0 is piece1 and piece1 is piece2:
        return piece0

    piece0 = board[index_of(2, 0)]
    piece1 = board[index_of(1, 1)]
    piece2 = board[index_of(0, 2)]
    if piece0 is not None and piece0 is piece1 and piece1 is piece2:
        return piece0

    return None

def play() -> None:
    players = get_players()

    board = [None] * 9
    turn = Piece.Cross
    winner = None
    while winner is None and None in board:
        display_header(board)

        player = players[turn]
        x, y = get_human_input(turn) if player is Player.Human else get_computer_input(turn, board)
        valid_input = x is not None and y is not None and is_in_bounds(x, y)
        if not valid_input:
            continue

        if is_space_free(board, x, y):
            board[index_of(x, y)] = turn
            winner = find_winner(board)
            turn = Piece.Cross if turn is Piece.Naught else Piece.Naught

    display_end_screen(board, winner)

play()