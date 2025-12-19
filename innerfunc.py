#Create an inner function
def outer_func(a,b):
    def inner_func():
        return a+b
    result = inner_func() + 5
    return result
print(outer_func(10,20))

