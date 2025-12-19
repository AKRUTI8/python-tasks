#Calculate the sum and average of the digits present in a string
str1 = "PYnative298496"
sum = 0
num = 0
avg = 0
for ch in str1:
    if ch.isdigit():
        num  = int(ch)
        sum = sum + num
        avg = sum / num 
print(sum)   
print(avg) 