# Question 10
# ===========
# Write a program that accepts a sequence of whitespace separated words as input and prints the words 
# after removing all duplicate words and sorting them alphanumerically.

# def sort_words():
#     words = input().split(" ")
#     res = list({item for item in words})
#     return " ".join(sorted(res))
#
#
# print(sort_words())

# Question 11
# ===========
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then
# check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma
# separated sequence.

def check_div_five():
    nums = input().split(",")
    res = [num for num in nums if int(num, 2)%5==0]
    return ','.join(res)

print(check_div_five())