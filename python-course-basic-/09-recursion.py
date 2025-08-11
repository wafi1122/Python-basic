def iterativeFuctorial(n):
    result = 1
    for i in range(n ,0 , -1):
        result = result * i
    return result 
print(iterativeFuctorial(5))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
    
    