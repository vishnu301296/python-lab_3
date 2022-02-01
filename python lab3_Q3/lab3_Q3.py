#Write a Python program to append text to a file and display the text


ans = open("ans.txt","a")
ans.write(input("Enter your Name : "))
ans.close()

ans = open("ans.txt" , "r")
print(ans.read())