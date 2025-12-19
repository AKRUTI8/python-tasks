#Find the sum of a series of a number up to n terms
num = 2
terms = 5

sum = 0
currentnum = 0

for i in range(1,terms+1):
    currentnum = currentnum * 10 + num
    sum = sum + currentnum
print(sum)
