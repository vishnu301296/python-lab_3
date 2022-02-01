#Write a Python program to read a random line from a file.

import random
def randnum(fname):
	lines=open(fname).read().splitlines()
	print(lines)
	return random.choice(lines)

print(randnum('c:/Users/VISHNU S/Desktop/project/python/python lab_3/python lab3_Q15/ans.txt'))