#Create a function with keyword arguments
def print_info(**kwargs):
    for key,value in kwargs.items():
        print(" ", key + ":", value)

print(print_info(name="akruti",age="21"))    