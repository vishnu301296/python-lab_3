#Write a Python program to read a file line by line store it into a variable

ans = " hi guys \n welcome to python learning\n"

f = open('ans.txt', "a")
f.writelines(ans)
f.close()
 

f = open('ans.txt', 'r')
lines = f.readlines()

for x in lines :
    print(x.strip())