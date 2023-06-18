# Fibonacci
# f(0) = 0
# f(1) = 1
# f(2) = f(0) + f(1)
# f(n) = f(n-1) + f(n-2)

n=6

def fibonacci(n):
    if ( n == 1 ):
        return 1
    elif ( n == 0):
        return 0
    else:
        return(fibonacci(n-1)+fibonacci(n-2))



while (n >=0 ):
    print(fibonacci(n))
    n = n - 1







# def printSeq (n):
#     if ( n ==1 ):
#         print(0)
#     else:
#         print    


# fibonacci(4)+fibonacci(3)
# fibonacci(3)+fibonacci(3)+fibonacci(2)+fibonacci(1)

# def fibonacciSeq (n):
#     if (n == 0):
#         print(0)
#     elif (n ==1):
#         print (0, 1)    
#     else:
#         print(fibonacciSeq(n -1))
# fibonacciSeq(7)    

# print(f"Fibonacci value at {n} place is",fibonacci(n))