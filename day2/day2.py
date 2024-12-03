import csv

#Function for part 1 of the problem
def func1(matrix):
    safeReports = 0

    def checkRow(row):
        incrementArr = []

        for index, num in enumerate(row[:-1]):
            if abs(int(row[index + 1]) - int(row[index])) == 0 or abs(int(row[index + 1]) - int(row[index])) > 3:
                return 0
            else:
                if int(row[index + 1]) - int(row[index]) < 0:
                    incrementArr.append(-1)
                elif int(row[index + 1]) - int(row[index]) > 0:
                    incrementArr.append(1)

                if index == 0:
                    continue
                else:
                    if incrementArr[-1] != incrementArr[-2]:
                        return 0
        return 1

    for row in matrix:
        safeReports += checkRow(row)

    return safeReports

def test():
    testMatrix = [["7","6","4","2","1"],
                  ["1","2","7","8","9"],
                  ["9","7","6","2","1"],
                  ["1","3","2","4","5"],
                  ["8","6","4","4","1"],
                  ["1","3","6","7","9"]]

    print(f"\nTest matrix: \n")

    for row in testMatrix:
        print(f"\t{row}")

    print(f"\n\tSafe reports: {func1(testMatrix)}")

def main():
    matrix = []

    with open("dataDay2.csv") as fileObject:
        data = csv.reader(fileObject, delimiter=' ')

        for row in data:
            matrix.append(row)

    print(f"\n\tSafe reports: {func1(matrix)}")

if __name__ == '__main__':
    print(f"\nTEST CASE")
    test()

    print(f"\nSOLUTION")
    main()

