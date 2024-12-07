
class Guard:
    def __init__(self, row, col, direction):
        self.row = row
        self.col = col
        self.direction = direction
        self.visited = []

    def move(self, back=False):
        if self.direction == "^":
            self.row -= 1

        elif self.direction == ">":
            self.col += 1

        elif self.direction == "v":
            self.row += 1

        elif self.direction == "<":
            self.col -= 1

        if not back:
            self.visited.append((self.row, self.col))

    def rotate90(self):
        if self.direction == "^":
            self.direction = ">"

        elif self.direction == ">":
            self.direction = "v"

        elif self.direction == "v":
            self.direction = "<"

        elif self.direction == "<":
            self.direction = "^"

    def rotate180(self):
        if self.direction == "^":
            self.direction = "v"

        elif self.direction == ">":
            self.direction = "<"

        elif self.direction == "v":
            self.direction = "^"

        elif self.direction == "<":
            self.direction = ">"

def func1(patrolMap):

    rowInit = 0
    colInit = 0
    directionInit = ""

    for row in range(len(patrolMap)):
        for col in range(len(patrolMap[0])):
            if (patrolMap[row][col] == "^" or
                    patrolMap[row][col] == "v" or
                    patrolMap[row][col] == "<" or
                    patrolMap[row][col] == ">"):

                rowInit = row
                colInit = col
                directionInit = patrolMap[row][col]

    guard = Guard(rowInit, colInit, directionInit)

    while True:

        if guard.direction == "^" and guard.row == 0:
            break
        elif guard.direction == ">" and guard.col == len(patrolMap[0]) - 1:
            break
        elif guard.direction == "v" and guard.row == len(patrolMap) - 1:
            break
        elif guard.direction == "<" and guard.col == 0:
            break

        guard.move()

        if patrolMap[guard.row][guard.col] == "#":
            guard.visited.pop(-1)
            guard.rotate180()
            guard.move(back=True)
            guard.rotate180()
            guard.rotate90()

    return len(set(guard.visited))

def test():
    testMap = [[".",".",".",".","#",".",".",".",".","."],
               [".",".",".",".",".",".",".",".",".","#"],
               [".",".",".",".",".",".",".",".",".","."],
               [".",".","#",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".","#",".","."],
               [".",".",".",".",".",".",".",".",".","."],
               [".","#",".",".","^",".",".",".",".","."],
               [".",".",".",".",".",".",".",".","#","."],
               ["#",".",".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".","#",".",".","."]]

    print(f"Test matrix")
    for row in testMap:
        print(row)

    print(f"\nDistinct positions visited: {func1(testMap)}")

if __name__ == "__main__":
    test()

