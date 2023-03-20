from math import sqrt

# Question 4
# ==========
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple
# which contains
# every number.Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

my_input = input()
print(my_input.split(','))
print(tuple(my_input.split(',')))


# Question 5
# ==========
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also, please include simple test function to test the class methods.

class MyString():
    def getString(self):
        self.msg = input()

    def printString(self):
        print(self.msg.upper())


def test_func():
    res = MyString()
    msg = res.getString()
    return res.printString()


test_func()

# Question 6
# ==========
# Write a program that calculates and prints the value according to the given formula:
#       Q = Square root of [(2 _ C _ D)/H]
# Following are the fixed values of C and H: C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# If the output received is in decimal form, it should be rounded off to its nearest value (for example,
# if the output received is 26.0, it should be printed as 26).In case of input data being supplied to the
# question, it should be assumed to be a console input.

D = input().split(',')


def calc_area(item):
    C, H = 50, 30
    return sqrt((2 * C * item) / H)


res = [str(round(calc_area(float(item)))) for item in D]
print(','.join(res))

# Question 7
# ==========
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value
# in the i-th row and j-th column of the array should be i _ j.*
# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
# Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

i, j = input().split(',')
row_idxs = [item for item in range(int(i))]
col_idxs = [item for item in range(int(j))]
for i in row_idxs:
    row = []
    for j in col_idxs:
        row.append(i * j)
    print(row, end=",")

# Question 8
# ==========
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
# sequence after sorting them alphabetically.

words = input().split(',')
print(','.join(sorted(words)))

# Question 9
# ==========
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the
# sentence capitalized.
res = []
while True:
    text = input()
    if text == '':
        break
    else:
        res.append(text.upper())
print(" \n".join(res))
