#Find largest and smallest digit in a number
num = -4853
num = abs(num)
max = 0
min = None
temp = 0
while num>0:
    temp = num % 10
    if max<temp:
        max=temp
    if min is None:
        min = temp
    else:
        if temp < min:
            min = temp
    num = num // 10     
print(max,min)
