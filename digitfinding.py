str = input('Enter a string: ')
for ch in str:
    if ch.isdigit():
        print("The string contains digit.")
        break
else:
    print("The string does not contain any digits.")
        