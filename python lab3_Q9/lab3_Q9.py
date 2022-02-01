#Write a Python program to count the number of lines in a text file.

with open(
    "c:/Users/VISHNU S/Desktop/project/python/python lab_3/python lab3_Q9/ans.txt", 'r') as f:
    for count, line in enumerate(f):
        pass
print('Total Lines', count + 1)