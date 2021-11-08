from typing import List

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
    i = 0
    for row in table:
        i += 1
        if i == 1:
            print('-'*19)
        print('|', end='')
        for x in row:
            if x == 0:
                print('.', end=' ')
            else:
                print(x, end=' ')
        print('|')
        if i == 9:
            print('-'*19)
    return

def readMove() -> dict:
    move = {
        "row" : 0,
        "col" : 0,
        "val" : 0
    }
    # read the actual values
    input()
    return move

def isCompleted(table: List[List[int]]) -> bool:
    return False

def isValidMove(move: dict, table: List[List[int]]) -> bool:
    return True

def main():
    original = readFromFile('sudoku.txt')
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

'''
table = {
    "1:1" : 7,
    "1:2" : 0,
}

print(table)
table[f"{move['row']}:{move['col']}"] = move['val']
#table[ str(move['row']) + ':' + str(move['col']) ] = move['val']
print(table)
'''