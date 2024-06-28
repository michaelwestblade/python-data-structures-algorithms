def factorial(n):
    # base case
    if n == 1:
        return 1
    # iterate
    return n * factorial(n - 1)

print(factorial(5))

# 4!
# 4 x 3!
# 4 x 3 x 2!
# 4 x 3 x 2 x 1!
# 4 x 3 x 2 x 1

"""
CALL STACK
factorial(1) return 1
factorial(2) return 2 * factorial(1)
factorial(3) return 3 * factorial(2)
factorial(4) return 4 * factorial(3)

return 4 * 3 * 2 * 1
"""

print(factorial(20))