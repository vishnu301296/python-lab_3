#Write a Python program to read a file line by line store it into an array.


list = ["hi guys\n","welcome to python learning\n","Have a nice day\n","Good luck\n"]

f = open('ans.txt', 'a')
f.writelines(list)
f.close()
 

f = open('ans.txt', 'r')
lines = f.readlines()

for x in lines :
    print(x.strip())