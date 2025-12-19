#Modifies global variable
global_var = 10
def my_func():
    global global_var 
    global_var = 20
    return global_var
    
print(my_func())
print(global_var)    