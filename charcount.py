#Count all letters, digits, and special symbols from a given string
str1 = "P@#yn26at^&i5ve"
letters = 0
digits = 0
symbols = 0
for ch in str1:
    if ch.isdigit():
        digits+=1
    elif ch.isalpha():
        letters+=1
    elif not ch.isalnum():
        symbols+=1
print("letters",letters)
print("digits",digits)
print("symbols",symbols)                 