def climbStairs(n):
    # Base cases
    if n == 1:
        return 1
    if n == 2:
        return 2

    # Initialize the first two steps
    a, b = 1, 2

    # Calculate ways for each step from 3 to n
    for i in range(3, n + 1):
        a, b = b, a + b  # a is f(n-2), b is f(n-1)

    return b  # f(n) is stored in b

# Example usage:
print(climbStairs(2))  # Output: 2
print(climbStairs(3))  # Output: 3
print(climbStairs(4))  # Output: 5