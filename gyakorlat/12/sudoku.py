from typing import List
from typing import Dict

# Feladat: Implementald a readMove, isValidMove, es isCompleted fuggvenyeket

def readFromFile(fname: str) -> List[List[int]]:
    '''Returns a 9x9 matrix as a list of lists'''
    table = []
    with open(fname) as f:
        for line in f:
            #row = line.split()
            #for i in range(len(row)):
            #    row[i] = int(row[i])
            row = [int(i) for i in line.split()]
            table.append(row)
    return table

def printTable(table: List[List[int]]):
    print('   ', end='')
    for i in range(1, 10):
        print(i, end=' ')
    print('')
    i = 0
    for row in table:
        i += 1
        if i == 1:
            print('-'*21)
        print(i, end=' |')
        j = 0
        for x in row:
            if x == 0:
                print('.', end='')
            else:
                print(x, end='')
            j += 1
            if j % 3 == 0:
                print('|', end='')
            else:
                print(' ', end='')
        print('')
        if i % 3 == 0:
            print('-'*21)
    return

def readMove() -> Dict[str, int]:
    move = {
        "row" : 0, # row index
        "col" : 0, # column index
        "val" : 0  # value to write into the cell, or 0 to clear cell
    }
    line = input()
    # TODO: get the move values from the input line
    # feltetelezheto, hogy helyes formatumu a bemenet:
    # 3 db egesz szam, szokozokkel elvalasztva
    return move

def isCompleted(table: List[List[int]]) -> bool:
    # TODO
    return False

def isValidMove(move: Dict[str, int], table: List[List[int]]) -> bool:
    # TODO
    return True

def main():
    original = readFromFile('sudoku1.txt')
    table = list(original)

    while not isCompleted(table):
        printTable(table)
        move = readMove()
        row = move['row']
        col = move['col']
        if original[row][col] != 0:
            print("Error: That cell cannot be overriden.")
        elif not isValidMove(move, table):
            print("Wrong move!")
        else:
            table[row][col] = move['val']
    printTable(table)
    print("Congratulations!")


if __name__ == "__main__":
    main()
