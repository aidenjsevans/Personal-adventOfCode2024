
def func1(stringMatrix):
    xmasCount = 0
    n = len(stringMatrix)

    rowContatString = ""
    colContatString = ""
    diagContatString = ""
    antiDiagContatString = ""

    #Make new string consisting of all rows in series
    for row in stringMatrix:
        for char in row:
            rowContatString += char

    #Make new string consisting of all columns in series
    for colIndex in range(n):
        for rowIndex in range(n):
            colContatString += stringMatrix[rowIndex][colIndex]
    
    #Make new string consisting of all diagonals in series
    for rowIndex in range(n):
        row, col = rowIndex, 0

        while row < n and col < n:
            diagContatString += stringMatrix[row][col]
            row += 1
            col += 1

    for colIndex in range(1, n):
        row, col = 0, colIndex

        while row < n and col < n:
            diagContatString += stringMatrix[row][col]
            row += 1
            col += 1

    stringArr = [rowContatString, colContatString, diagContatString]

    for string in stringArr:
        xmasCount += string.count("XMAS")
        xmasCount += string.count("SAMX")

    print(rowContatString)
    print(colContatString)
    print(diagContatString)
    print(xmasCount)

def test():
    testStringMatrix = ["MMMSXXMASM",
                        "MSAMXMSMSA",
                        "AMXSXMAAMM",
                        "MSAMASMSMX",
                        "XMASAMXAMM",
                        "XXAMMXXAMA",
                        "SMSMSASXSS",
                        "SAXAMASAAA",
                        "MAMMMXMMMM",
                        "MXMXAXMASX"]

    func1(testStringMatrix)

if __name__ == "__main__":
    test()














