from typing import Dict
from functools import lru_cache
memo: Dict[int, int] = {0:0, 1:1}

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]

@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n - 2) + fib4(n - 1)

if __name__ == "__main__":
    print(fib4(5))
    print(fib4(50))
