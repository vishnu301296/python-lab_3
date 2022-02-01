#Write a Python program to combine each line from first file with the corresponding line in second file.

with open('c:/Users/VISHNU S/Desktop/project/python/python lab_3/python lab3_Q14/ans.txt') as f1,open('c:/Users/VISHNU S/Desktop/project/python/python lab_3/python lab3_Q14/second.txt') as f2:
	for l1,l2 in zip(f1,f2):
		# print(l1+l2)
		
		print(l1+l2)