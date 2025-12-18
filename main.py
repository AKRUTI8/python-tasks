#Find the number of occurrences of a substring in a string

str_x = "Emma is good developer. Emma is a writer"
count=0
target = 'Emma'
# print(str_x.split(" "))

for s in str_x.split(" "):
    print(s)      
    if s == target:
        count+=1
print(count)       