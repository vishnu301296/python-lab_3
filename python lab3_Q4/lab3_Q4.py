#Write a Python program to read last n lines of a file.



def read_lastnlines(fname,n):
	with open('c:/Users/VISHNU S/Desktop/project/python/python lab_3/python lab3_Q4/ans.txt') as f:
		for line in (f.readlines() [-n:]):
			print(line)

read_lastnlines('ans.txt',1)