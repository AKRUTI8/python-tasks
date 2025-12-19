#Append new string in the middle of a given string
#AuKellylt
#s1 = "Aulty"
#s2 = "Kelly"

#s3 = s1[:len(s1)//2] + s2 + s1[len(s1)//2:]
#print(s3)

s1 = "Weekend"
s2 = "DAY"
result = ""
n = len(s1)

if n % 2 == 0:
    middle = n // 2-1
    result = s1[:middle] + s2 + s1[middle+1:]
else: 
    middle = n // 2
    result = s1[:middle] + s2 + s1[middle+1:]
print(result)    
