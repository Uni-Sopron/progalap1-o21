import json
from typing import List
import random

def make_empty_board(width: int, height: int) -> List[List[bool]]:
    board = []
    for _ in range(height):
        #board.append([False for _ in range(width)])
        row = []
        for _ in range(width):
            row.append(False)
        board.append(row)
    return board

def fill_board(board: List[List[bool]], percent: float) -> None:
    for row in range(len(board)):
        for cell in range(len(board[row])):
            if random.random() <= percent/100:
                board[row][cell] = True

def fill_board2(board: List[List[bool]], alive_count: int) -> None:
    # TODO
    pass

def read_board(filename: str) -> List[List[bool]]:
    # TODO
    return []

def print_board(board: List[List[bool]], alive_char: str, dead_char: str) -> None:
    for row in board:
        for cell in row:
            if cell:
                print(alive_char, end='')
            else:
                print(dead_char, end='')
        print('')

def alive_neighbors(board: List[List[bool]], row: int, col: int) -> int:
    count = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i == row and j == col:
                continue
            if i >= len(board) or i < 0:
                continue
            if j >= len(board[i]) or j < 0:
                continue
            if board[i][j]:
                count += 1
    return count

def next_generation(board: List[List[bool]]) -> List[List[bool]]:
    new_board = []
    for row in range(len(board)):
        new_board.append([])
        for cell in range(len(board[row])):
            n = alive_neighbors(board, row, cell)
            if board[row][cell]:
                if n < 2 or n > 3:
                    new_board[row].append(False)
                else:
                    new_board[row].append(True)
            elif n == 3:
                new_board[row].append(True)
            else:
                new_board[row].append(False)
    return new_board

def main():
    config = json.load(open('config.json'))
    width = config['width']
    height = config['height']
    if 'alive_percent_start' in config:
        board = make_empty_board(width, height)
        fill_board(board, config['alive_percent_start'])
    elif 'alive_count_start' in config:
        board = make_empty_board(width, height)
        fill_board2(board, config['alive_count_start'])
    elif 'initial_board' in config:
        board = read_board(config['initial_board'])
    for round in range(config['num_rounds']):
        print('Round', round)
        print_board(board, config['alive'], config['dead'])
        board = next_generation(board)
        input()
    print('At the end:')
    print_board(board, config['alive'], config['dead'])

if __name__ == "__main__":
    main()
