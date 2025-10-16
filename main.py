#read data

def readData(filepath):
    with open(filepath, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    # len_x, len_y = map(int, lines[0].split()) # Parse lengths (not used)
    gap_cost, mismatch_cost = map(int, lines[1].split())
    x = lines[2]
    y = lines[3]
    return x, y, gap_cost, mismatch_cost


def generateMatrix(x,y,gap_cost,mismatch_cost):
    matrix = [[0] * (len(x)+1) for _ in range(len(y)+1)] #initalize 2d array with all 0s. #it's one bigger because we have an extra starting row/col for the base cases that are just adding mismatch cost each time
    #generate first row and column as the letters
    """
    for i in range(len(x)):
        matrix[0][i+1]=x[i:i+1]
    for i in range(len(y)):
        matrix[i+1][0]=y[i:i+1]
    """

    #gen first row and col:
    for i in range(len(x)):
        matrix[0][i+1]=matrix[0][i]-mismatch_cost
    for i in range(len(y)):
        matrix[i+1][0]=matrix[i][0]-mismatch_cost

    #fill in matrix
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[i])):
            #decide what number to put in
            matrix[i][j]=9

    return matrix

def printMatrix(matrix):
    print("Matrix:")
    for row in matrix:
        print(' '.join(str(cell) for cell in row))


#main:
x,y,gap_cost,mismatch_cost=readData('data2.txt')
print(x,y,gap_cost,mismatch_cost)

matrix=generateMatrix(x,y,gap_cost,mismatch_cost)
printMatrix(matrix)