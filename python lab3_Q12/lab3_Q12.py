#Write a Python program to write a list to a file.


ans = ["python","java","Css",]


with open('c:/Users/VISHNU S/Desktop/project/python/python lab_3/python lab3_Q12/lab.txt', "w") as myfile:
        for x in ans:
                myfile.write("%s\n" % x)

with open("c:/Users/VISHNU S/Desktop/project/python/python lab_3/python lab3_Q12/lab.txt" , "r")as seen:

       print(seen.read())