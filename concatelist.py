#Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
l3=[]
for l1,l2 in zip(list1,list2):
    out=l1+l2
    l3.append(out)
print(l3)
    
