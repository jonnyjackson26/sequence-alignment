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
            #for each cell, decide what number to put in
            x_char, y_char = x[j-1], y[i-1]

            diagonal = matrix[i-1][j-1] + (1 if x_char == y_char else -mismatch_cost) #match #assuming 1 is the reward for matching characters
            gap_on_x=matrix[i][j-1]-gap_cost    #pull down 
            gap_on_y=matrix[i-1][j]-gap_cost    #pull down 

            matrix[i][j]=max(diagonal, gap_on_x, gap_on_y) #take the optimal solution between either pulling down on x, y, or taking the diagnol

    return matrix


def printMatrix(matrix):
    print("Matrix:")
    # Find max width for formatting
    max_width = max(len(str(cell)) for row in matrix for cell in row)
    for row in matrix:
        print(' '.join(f"{str(cell):>{max_width}}" for cell in row))


def findBestPathThruMatrix(matrix, x, y, gap_cost, mismatch_cost):
    # Start at bottom-right corner
    i, j = len(y), len(x)
    x_alignment, y_alignment = "", ""
    totalAlignmentScore=0

    while i > 0 and j > 0:
        current = matrix[i][j]
        diagonal = matrix[i-1][j-1]
        up = matrix[i-1][j]
        left = matrix[i][j-1]

        if current == diagonal + (1 if x[j-1] == y[i-1] else -mismatch_cost):
            # came from diagonal (match or mismatch)
            x_alignment = x[j-1] + x_alignment
            y_alignment = y[i-1] + y_alignment
            totalAlignmentScore=totalAlignmentScore + (0 if x[j-1] == y[i-1] else +mismatch_cost)
            i -= 1
            j -= 1
        elif current == up - gap_cost:
            # came from up — gap in y
            x_alignment = "-" + x_alignment
            y_alignment = y[i-1] + y_alignment
            i -= 1
            totalAlignmentScore=totalAlignmentScore+gap_cost
        else:
            # came from left — gap in x
            x_alignment = x[j-1] + x_alignment
            y_alignment = "-" + y_alignment
            j -= 1
            totalAlignmentScore=totalAlignmentScore+gap_cost

    # if we still have remaining characters in x or y, pad them with gaps
    while j > 0:
        x_alignment = x[j-1] + x_alignment
        y_alignment = "-" + y_alignment
        j -= 1
        totalAlignmentScore=totalAlignmentScore+gap_cost
    while i > 0:
        x_alignment = "-" + x_alignment
        y_alignment = y[i-1] + y_alignment
        i -= 1
        totalAlignmentScore=totalAlignmentScore+gap_cost

    print("Optimal alignment:")
    print(x_alignment)
    print(y_alignment)
    print(f"Score: {totalAlignmentScore}")



#main:
x,y,gap_cost,mismatch_cost=readData('data.txt')
print(f"Gap cost: {gap_cost}\nMismatch cost: {mismatch_cost}\nx: {x}\ny: {y}\n")


matrix=generateMatrix(x,y,gap_cost,mismatch_cost)
printMatrix(matrix)

findBestPathThruMatrix(matrix, x, y, gap_cost, mismatch_cost)