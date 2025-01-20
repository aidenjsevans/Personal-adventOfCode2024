
def func1(diskMap):
    blockArr = []
    ID = 0

    for index, num in enumerate(diskMap, 1):

        if index % 2 != 0:
            for _ in range(num):
                blockArr.append(ID)
            ID += 1
        else:
            for _ in range(num):
                blockArr.append(".")

    stack = []

    while blockArr:
        if blockArr[0] != ".":
            stack.append(blockArr.pop(0))
        else:
            while True:
                if blockArr[-1] != ".":
                    

    return blockArr


def test():
    testDiskMap = [1,2,3,4,5]
    print(func1(testDiskMap))

if __name__ == '__main__':
    test()




