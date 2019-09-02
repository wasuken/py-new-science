from collections import defaultdict

memo = {0:0,1:1}

def fib(n: int) -> int:
    if memo.get(n) == None:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

if __name__ == '__main__':
    print(fib(4))
    print(fib(40))
    print(fib(100))
