# Question 5
# ==========
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains 
# every number.Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

my_input = input()
print(my_input.split(','))
print(tuple(my_input.split(',')))

# Question 6
# ==========
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

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
