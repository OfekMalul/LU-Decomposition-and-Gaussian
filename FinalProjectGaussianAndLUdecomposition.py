# main menu
def mainMenu():
    print("Welcome:")
    print("To run the program for Gaussian Elimination enter 1:")
    print("To run the program for LU-Decomposition enter 2:")
    print("To Quit the program enter 3:")

# calculate the factor
def calcFactor(x, pivotVector):
    global nop
    nop += 2
    return (-1 * x) / pivotVector

# calculate each element of the row
def calcElement(x, factor, pivot):
    global nop
    nop += 2
    return x + factor * pivot

# calculate the soluion for each x (backward substitution)
def calcFinalResultForX(constant, sumx, y):
    global nop
    nop += 2
    return (constant - sumx) / y


r = 0
while r == 0:
    # Print main menu
    mainMenu()
    c = int(input())
    # Counter for numbers of operations
    nop = 0
    if c == 1:
        print("You have picked Gaussian Elimination:")
        print("")

        # Changes the row by another row for matricxA and matricxB
        def changeRow(matrixA, matrixB, i):
            emptyRow = matrixA[i]  # empty element saves the pivot row with the zero
            matrixA[i] = matrixA[i + 1]  # pivot row becomes the row under the pivot row
            matrixA[i + 1] = emptyRow  # The row under the pivot becomes the pivot row

            emptyVector = matrixB[i]  # Same as above just for matricxB.
            matrixB[i] = matrixB[i + 1]
            matrixB[i + 1] = emptyVector


        # Gets the user matrixA input
        RC = int(input("Enter the number of rows and columns:"))
        # Initialize matrix
        matrixA = []
        print("Enter the entries:")
        # For user input
        for i in range(RC):  # A for loop for row entries
            a = []
            for j in range(RC):  # A for loop for column entries
                a.append(int(input()))
            matrixA.append(a)

        # For printing the matrix
        for i in range(RC):
            for j in range(RC):
                print(matrixA[i][j], end=" ")
            print()

        # creating an empty list
        matrixB = []
        print('Please put the right vector')
        # iterating till the range
        for i in range(0, RC):
            ele = int(input())
            matrixB.append(ele)  # adding the element
        print(matrixB)
        # Gives the size of the matricx
        numRows = len(matrixB)
        x = [0, 0, 0]
        #k - this is the index of the fix row
        for k in range(numRows - 1):  # pivot row
            # i - this is the index of the row to change
            for i in range(k + 1, numRows):  # row under pivot
                # there is no need to do anything if the element is already 0
                if (matrixA[i][k] == 0 and i <= numRows - 2):
                    changeRow(matrixA, matrixB, i)
                # calculating the factor variable m by the use of a function
                factor = calcFactor(matrixA[i][k], (matrixA[k][k]))
                # j - index of the columns
                for j in range(k, numRows):  # column
                    # calculating the element using the factor
                    matrixA[i][j] = calcElement(matrixA[i][j], factor, matrixA[k][j])
                matrixB[i] = calcElement(matrixB[i], factor, matrixB[k])

        # Back substitution
        # calculates the last x.
        x[numRows - 1] = matrixB[numRows - 1] / matrixA[numRows - 1][numRows - 1]
        nop += 1
        # i - row index
        for i in range(numRows - 2, -1, -1):  # the last -1 indicating the step.
            sumX = 0
            # j- column index
            for j in range(i + 1, numRows):
                sumX = sumX + matrixA[i][j] * x[j]  # calculate the value of the known constants
                nop += 2
            x[i] = calcFinalResultForX(matrixB[i], sumX, matrixA[i][i])
        print('The solution is')
        print(x)
        print('Number of operations:',nop)
        print("")

    elif c == 2:
        print("You have picked LU Decomposition")
        print("")
        
        # Gets the row metrix
        def getRowMatrix():
            arr = []
            # looping over the array to get the number of rows
            for i in range(numRows):
                arr.append(i)
            return arr

        # Calculates the Scaler metrix
        def getScalerMatrix():
            arr = []
            # first loop to go over each row in the matrix
            for i in range(numRows):
                row = matrixA[i]
                rowMax = 0  # will hold the max value from each row
                # 2nd loop to go over each element in the row to check what is the max value.
                for s in range(len(row)):
                    vector = abs(row[s])
                    if (vector > rowMax):
                        rowMax = vector
                arr.append(rowMax)
            return arr

        # checks if there is a need to change the row and returns the pivot.
        # Gets as an argument the index because we dont want to check all the rows every time.
        def rowChange(k):
            row = rowMatrix[k]
            maxVector = 0
            for i in range(k, numRows):
                # gets the absolute value of the vector and divides by the scaler matrix
                vector = abs(matrixA[rowMatrix[i]][k]) / scalerMatrix[rowMatrix[i]]
                if (vector > maxVector):
                    maxVector = vector
                    row = rowMatrix[i]  # changes row to the current row that holds the max vector
            # Check if the maximum is in the initial row or not
            if (row != k):
                initalIndex = rowMatrix.index(k)  # Gets the index of the row that corrolates to our old max
                newIndex = rowMatrix.index(row)  # Gets the index the row that corolates with our discovred new max
                del rowMatrix[initalIndex]  # removes the row index
                rowMatrix.insert(initalIndex, row)  # insert the row index of the new max into the new position
                del rowMatrix[newIndex]  # removes the the row index of the new max from the old position
                rowMatrix.insert(newIndex, k)  # adds the row index of our old max into the old positon of the new max
            return rowMatrix

            # Function to change the values of b matrix according to the changes of the row matrix

        def matrixBchange(k):
            vector = 0
            vectorIndex = 0
            vectorToMove = 0

            if (rowMatrix[k] != k):
                vector = matrixB[k]
                vectorIndex = rowMatrix.index(k)
                vectorToMove = matrixB[rowMatrix[k]]
                del matrixB[k]
                matrixB.insert(k, vectorToMove)
                del matrixB[rowMatrix[k]]
                matrixB.insert(vectorIndex, vector)


        # Gets the user matrixA input
        RC = int(input("Enter the number of rows and columns:"))
        # Initialize matrix
        matrixA = []
        print("Enter the entries:")
        # For user input
        for i in range(RC):  # A for loop for row entries
            a = []
            for j in range(RC):  # A for loop for column entries
                a.append(int(input()))
            matrixA.append(a)

        # For printing the matrix
        for i in range(RC):
            for j in range(RC):
                print(matrixA[i][j], end=" ")
            print()

        # creating an empty list
        matrixB = []
        print('Please put the right vector')
        # iterating till the range
        for i in range(0, RC):
            ele = int(input())
            matrixB.append(ele)  # adding the element
        print(matrixB)

        zMatrix = [0, 0, 0]
        xMatrix = [0, 0, 0]
        numRows = len(matrixA)
        # holds the value from the fuction row matrix
        rowMatrix = getRowMatrix()
        # holds the value from the function scaler matrix
        scalerMatrix = getScalerMatrix()

        # start of main program
        # k - this is the index of the fix row
        for k in range(numRows - 1):
            # change row vector if needed
            rowMatrix = rowChange(k)
            matrixBchange(k)
            # i - index of the rows to change
            for i in range(k + 1, numRows):
                # calculating the factor variable by the use of a fucntion
                factor = calcFactor(matrixA[rowMatrix[i]][k], matrixA[rowMatrix[k]][k])
                # j - index of the columns
                for j in range(k, numRows):
                    if (
                            j == k):  # Calculates the first vector under the pivot according to the need of the lower and upper matrix.
                        matrixA[rowMatrix[i]][j] = factor * -1
                        nop += 1
                    else:
                        matrixA[rowMatrix[i]][j] = calcElement(matrixA[rowMatrix[i]][j], factor,
                                                               matrixA[rowMatrix[k]][j])  # calcualte the vectors
        # forward substitution
        # calculates the first z.
        zMatrix[0] = matrixB[0]
        # i - this is the row index
        for i in range(1, numRows):
            sumZ = 0
            # j- this is the column index
            for j in range(0, i):
                sumZ = sumZ - matrixA[rowMatrix[i]][j] * zMatrix[j]  # calculate the value of the known constants
                nop += 2
            zMatrix[i] = matrixB[i] + sumZ
            nop += 1

        # Back substitution
        # calculates the last x.
        xMatrix[numRows - 1] = zMatrix[numRows - 1] / matrixA[rowMatrix[numRows - 1]][numRows - 1]
        nop += 1
        # i - this is the row index
        for i in range(numRows - 2, -1, -1):  # the last -1 indicating the step.
            sumX = 0
            # j- this is the column index
            for j in range(i + 1, numRows):
                sumX = sumX + matrixA[rowMatrix[i]][j] * xMatrix[j]  # calculate the value of the known constants
                nop += 2
            xMatrix[i] = calcFinalResultForX(zMatrix[i], sumX, matrixA[rowMatrix[i]][i])
        print('The solution is')
        print(xMatrix)
        print('Number of operations:', nop)
        print("")

    elif c == 3:
        print("Have a good day!")
        break

    else:
        print("Please enter a valid option.")
        print("")
