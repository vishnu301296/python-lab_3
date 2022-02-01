#Write a python program to find the longest words.

def longest_word(filename):
        file = open(filename,"r")
        words = file.read().split() 
     
        max_len = len(max(words,key = len))
        for x in words :
              if len(x)== max_len :
                 print(x)

longest_word('c:/Users/VISHNU S/Desktop/project/python/python lab_3/python lab3_Q8/ans.txt')