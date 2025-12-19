#List Comprehension for Numbers

my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]
new_list = []

for item in my_list:
    if type(item) == int:
        new_list.append(item)
print(new_list)        