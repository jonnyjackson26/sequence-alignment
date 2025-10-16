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

    #gen first row and col:
    for i in range(len(x)):
        matrix[0][i+1]=matrix[0][i]-gap_cost
    for i in range(len(y)):
        matrix[i+1][0]=matrix[i][0]-gap_cost

    #fill in matrix
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[i])):
            #decide what number to put in
            x_char = x[j-1]
            y_char = y[i-1]

            diagonal = matrix[i-1][j-1] + (1 if x_char == y_char else -mismatch_cost) #match #assuming 1 is the reward for matching characters
            gap_on_x=matrix[i][j-1]-gap_cost    #pull down 
            gap_on_y=matrix[i-1][j]-gap_cost    #pull down 

            matrix[i][j]=max(diagonal, gap_on_x, gap_on_y)


            
            

    return matrix

def printMatrix(matrix):
    print("Matrix:")
    for row in matrix:
        print(' '.join(str(cell) for cell in row))


#main:
x,y,gap_cost,mismatch_cost=readData('data2.txt')
print(f"Gap cost: {gap_cost}\nMismatch cost: {mismatch_cost}\nx: {x}\ny: {y}\n")

matrix=generateMatrix(x,y,gap_cost,mismatch_cost)
printMatrix(matrix)