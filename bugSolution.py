def my_function(x, memo={}):
    if x in memo:
        return memo[x]
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        result = my_function(x - 1, memo) + my_function(x - 2, memo)
        memo[x] = result
        return result

print(my_function(35)) #This will now work correctly