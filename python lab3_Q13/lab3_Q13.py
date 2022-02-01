#Write a Python program to copy the contents of a file to another file .

# open both files
with open('c:/Users/VISHNU S/Desktop/project/python/python lab_3/python lab3_Q13/ans.txt','r') as firstfile, open('c:/Users/VISHNU S/Desktop/project/python/python lab_3/python lab3_Q13/second.txt','w') as secondfile:
	

	for line in firstfile:
			
			# write content to second file
			secondfile.write(line)
#please check the second file(second.txt)...
#Note - only enter text on first file(ans.txt) and just create a new file (second .txt)without entering any text.After entering the above code the text will automatically copy from first file(ans.txt) to second file(second.txt)
        