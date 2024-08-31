def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    first = 0
    second = 1
    result = 0
    for i in range(n-1):
        result = first + second
        first = second
        second = result
    return result

print(fib(4))
print(fib(5))