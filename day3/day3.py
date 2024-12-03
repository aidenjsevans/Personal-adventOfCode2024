import re

#Function for part 1 of the problem
def func1(string):

    def mulFunc(substring):
        nums = (substring[4:-1]).split(",")
        num1 = int(nums[0])
        num2 = int(nums[1])

        return num1 * num2

    mulTotal = 0
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    validSubstrings = re.findall(pattern, string)

    for substring in validSubstrings:
        mulTotal += mulFunc(substring)

    return mulTotal

def test():
    testString = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    print(f"\n\tTest string: '{testString}'")
    print(f"\n\tResult multiplication sum: {func1(testString)}")

def main():

    with open("dataDay3.csv") as fileObject:
        string = fileObject.read()
        print(f"\n\tResult multiplication sum: {func1(string)}")

if __name__ == '__main__':
    print(f"\nTEST CASE")
    test()

    print(f"\nSOLUTION")
    main()
