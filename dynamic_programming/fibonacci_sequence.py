from typing import Union, Any, Optional

counter = 0


def fib(n):
    global counter
    counter += 1
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


memo = [None] * 100
optimized_counter = 0


def fib_optimized(n: int) -> Union[Optional[int], None]:
    global optimized_counter
    optimized_counter += 1

    if memo[n] is not None:
        return memo[n]

    if n == 0 or n == 1:
        return n
    memo[n] = fib_optimized(n - 1) + fib_optimized(n - 2)
    return memo[n]

bottom_up_counter = 0

def fib_bottom_up(n: int) -> int:
    global bottom_up_counter

    fib_list = [0, 1]

    for index in range(2, n + 1):
        bottom_up_counter += 1
        next_fib = fib_list[index - 1] + fib_list[index - 2]
        fib_list.append(next_fib)

    return fib_list[n]


n = 30
print(f"\nFib of {n} is {fib(n)}")
print(f"\nCounter: {counter}")

n = 30
print(f"\nFib of {n} is {fib_optimized(n)}")
print(f"\nCounter: {optimized_counter}")

print("".join([f"{str(x)}, " for x in memo if x is not None]))

print(f"\nFib of {n} is {fib_bottom_up(n)}")
print(f"\nCounter: {bottom_up_counter}")
