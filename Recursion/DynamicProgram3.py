# A naive recursive solution
def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result


# A memoized solution
def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1, memo) + fib_2(n-2, memo)
    memo[n] = result
    return result



# A bottom-up solution

def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None for _ in range(n+1)]
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

def fibo(n):
    if n == 0:
        return 1
    a = 0
    b = 1

    for i in range(2, n+1):
        c = a+b
        a = b
        b = c
    return c

if __name__ == '__main__':
    a = 12
    print(fibo(a))
