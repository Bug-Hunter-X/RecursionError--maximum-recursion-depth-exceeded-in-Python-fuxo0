def my_function(x):
    if x == 0:
        return 0  # This line is correct
    elif x == 1:
        return 1 # This line is correct
    else:
        return my_function(x - 1) + my_function(x - 2) # This line is the bug, it causes a stack overflow for larger inputs

print(my_function(35)) #this will cause RecursionError: maximum recursion depth exceeded