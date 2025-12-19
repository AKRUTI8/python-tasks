#Count Character Frequencies
string1 = 'jessa'
freq={}
for ch in string1:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1    
        
print(freq)        