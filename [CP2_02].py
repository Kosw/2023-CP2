def write_x():
    global x
    x = x - 123
    print("print function x : ", x)

x = 4123
print("Global x : ", x)
write_x()
print("func call Global x : ", x)

def print_func_a():
    print("Printing func_a")
def print_parameter(x):
    print ('Parameter X : ', x)
    return x

print("Print func_a & parameter")
a = print_func_a()
param = print_parameter(5)
print(a)
print(param)

# def print_func_a():
#     print("Printing func_a")
# def print_parameter(x):
#     print("Parameter x : ", x)
#     return x
# def exec_param_func(function):
#     print("I try execute param function...")
#     return function()
#
#
#
# print("Execute exec_param_func")
# param_a = exec_param_func(print_func_a())
# print(param_a)
#
# param_parameter = exec_param_func(print_parameter(5))