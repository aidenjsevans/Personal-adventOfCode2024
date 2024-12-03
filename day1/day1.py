import csv

# Function for part 1 of the problem
def func1(arr1, arr2):
    arr1.sort()
    arr2.sort()

    sumTotal = 0

    for index, num in enumerate(arr1):
        sumTotal += abs(num - arr2[index])

    return sumTotal

#Function for part 2 of the problem
def func2(arr1, arr2):
    numCount = {}
    total = 0

    for index, num in enumerate(arr1):
        if num in numCount:
            numCount[num][1] += 1
        else:
            numCount[num] = [0, 1]

    for index, num in enumerate(arr2):
        if num in numCount:
            numCount[num][0] += 1
        else:
            continue

    for key, value in numCount.items():
        total += key*value[0]*value[1]

    return total

def test():
    testArr1 = [3,4,2,1,3,3]
    print(f"\n\tArray 1: {testArr1}")

    testArr2 = [4,3,5,3,9,3]
    print(f"\tArray 2: {testArr2}")

    print(f"\n\tTotal distance: {func1(testArr1, testArr2)}")
    print(f"\tSimilarity score: {func2(testArr1, testArr2)}")

def main():
    arr1 = []
    arr2 = []

    with open("dataDay1.csv") as fileObject:
        data = csv.reader(fileObject, delimiter=' ')

        for row in data:
            arr1.append(int(row[0]))
            arr2.append(int(row[-1]))

    print(f"\n\tTotal distance: {func1(arr1, arr2)}")
    print(f"\tSimilarity score: {func2(arr1, arr2)}")

if __name__ == "__main__":
    print(f"\nTEST CASE")
    test()

    print(f"\nSOLUTION")
    main()
