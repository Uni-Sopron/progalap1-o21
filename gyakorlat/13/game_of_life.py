import json
from typing import List

def make_empty_board(width: int, height: int) -> List[List[bool]]:
    pass

def fill_board(board: List[List[bool]], percent: float) -> None:
    pass

def print_board(board: List[List[bool]], alive_char: str, dead_char: str) -> None:
    pass

def next_generation(board: List[List[bool]]) -> List[List[bool]]:
    pass

def main():
    config = json.load(open('config.json'))
    width = config['width']
    height = config['height']
    board = make_empty_board(width, height)
    fill_board(board, config['alive_percent_start'])
    for round in range(config['num_rounds']):
        print('Round', round)
        print_board(board, config['alive'], config['dead'])
        board = next_generation(board)
    print('At the end:')
    print_board(board, config['alive'], config['dead'])

if __name__ == "__main__":
    main()
