#Name: Aishwarya Narayanan
#Date: April 22, 2020
#Purpose: Canadian Computing Competition Junior Problem #4

#Get a text
t = input("Enter a text")
#Get a text to search for
s = input ("Enter the text to search for")
answer="no"

#Check if the text that is being searched for is in the original text
for count in range (len(s)):
    if s in t:
        answer="yes"
        break
    else:
        s = s[1] + s[2] + s[0]
        
print(answer)









