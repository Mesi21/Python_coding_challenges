# Question 1
# ==========
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 
# 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

for i in range(2000, 3201):
  if i % 7 == 0 and i % 5 != 0:
    print(i, end=',')

print("\b")

# Question 2
# ==========
# Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence
# on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

def fact(num):
  if num == 1 or num == 0:
    return 1
  return num*fact(num-1)
print(fact(8))
print(fact(int(input())))

# Question 3
# ==========
# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number
# between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the
# program: 8
# Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def make_dict(num):
  res_dict = {}
  for i in range(1, num+1):
    res_dict[i] = i*i
  return res_dict

print(make_dict(8))
print(make_dict(int(input())))