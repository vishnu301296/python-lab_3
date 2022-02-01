#Write a Python program to read first n lines of a file

from itertools import islice

with open("c:/Users/VISHNU S/Desktop/project/python/python lab_3/python lab3_Q2/ans.txt") as ans:

    final = list(islice(ans,1))

print(final)