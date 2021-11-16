def read_matrix(filename: str) -> list:
    with open(filename) as f:
        return [ [int(x) for x in line.split()] for line in f ]

def sum_submatrix(mtx, i, j, height, width):
    sum = 0
    for k in range(i, i+height):
        for l in range(j, j+width):
            sum += mtx[k][l]
    return sum

def max_submatrix(mtx, height=3, width=3) -> tuple:
    '''Returns the (row,col) index of the top left corner
        of the height*width submatrix with maximal sum.
        '''
    maxcoords = (0,0)
    max = sum_submatrix(mtx, 0, 0, height, width)
    for i in range(len(mtx)-height+1):
        for j in range(len(mtx[i])-width+1):
            sum = sum_submatrix(mtx, i, j, height, width)
            if sum >= max:
                max = sum
                maxcoords = (i,j)
                print(maxcoords, max)
    return maxcoords

if __name__ == '__main__':
    mtx = read_matrix('matrix.txt')
    print(max_submatrix(mtx))
    
    row = mtx[0]
    maxidx = 0
    for i in range(len(row)):
        if row[i] > row[maxidx]:
            maxidx = i
    print(f'Az elso sorban a(z) {maxidx+1}. elem a legnagyobb')
