#!/usr/bin/env python3
import unittest

def roundGrade(grade):

    if grade < 38:
        return grade
    else:
        if grade % 5 >=3:
            return grade + 5 - (grade % 5)
        else:
            return grade

# def testRoundGrade():
#     assert roundGrade(10) == 10
#     assert roundGrade(0) == 0
#     assert roundGrade(13) == 13
#     assert roundGrade(28) == 28
#     assert roundGrade(38) == 40
#     assert roundGrade(41) == 41
#     assert roundGrade(48) == 50
#     assert roundGrade(59) == 60
#     assert roundGrade(61) == 61
#     assert roundGrade(57) == 57
#     assert roundGrade(99) == 100
#     assert roundGrade(100) == 100
#     assert roundGrade(78) == 80
#     print("All tests passed :)")

def main():
    n = int(input().strip())

    for i in range(n):
        print(roundGrade(int(input().strip())))


if __name__ == '__main__':
    # testRoundGrade()
    main()
