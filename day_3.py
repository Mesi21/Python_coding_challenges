# Question 10
# ===========
# Write a program that accepts a sequence of whitespace separated words as input and prints the words 
# after removing all duplicate words and sorting them alphanumerically.

def sort_words():
    words = input().split(" ")
    res = list({item for item in words})
    return " ".join(sorted(res))


print(sort_words())
