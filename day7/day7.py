import itertools

def func1(targets, numMatrix):
    globalVal = 0

    def calibrationResult(target, numArr):
        operations = {0: "*",
                      1: "+"}

        binMatrix = list(map(list, itertools.product([0, 1], repeat=len(numArr)-1)))
        print(binMatrix)

        for comb in binMatrix:
            val = 0

            for index in range(len(comb)):
                operation = operations[comb[index]]

                if index == 0:
                    if operation == "*":
                        val += (numArr[index] * numArr[index + 1])
                    elif operation == "+":
                        val += (numArr[index] + numArr[index + 1])
                else:
                    if operation == "*":
                        val *= numArr[index + 1]
                    elif operation == "+":
                        val += numArr[index + 1]

            if val == target:
                print(val)
                return val

        print(0)
        return 0

    for index in range(len(targets)):
        globalVal += calibrationResult(targets[index], numMatrix[index])

    return globalVal


def test():

    testTargets = [190, 3267, 83, 156, 7290, 161011, 192, 21037, 292]

    testNumMatrix = [[10, 9],
                     [81, 40, 27],
                     [17, 5],
                     [15, 6],
                     [6, 8, 6, 15],
                     [16, 10, 13],
                     [17, 8, 14],
                     [9, 7, 18, 13],
                     [11, 6, 16, 20]]

    calibrationTotal = func1(testTargets, testNumMatrix)
    print(f"\n{calibrationTotal}")

if __name__ == '__main__':
    test()
