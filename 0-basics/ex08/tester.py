from ft_filter import ft_filter

# With a function: keep only even numbers.
assert list(ft_filter(lambda n: n % 2 == 0, range(6))) == [0, 2, 4]

# With None: keep the original values that are truthy.
assert list(ft_filter(None, [0, 1, "", "hello", None])) == [1, "hello"]

# Check the exact docstring, including line breaks.
assert ft_filter.__doc__ == filter.__doc__

def is_even(n):
    print(f"Checking {n}")
    return n % 2 == 0

result = ft_filter(is_even, range(6))  # Prints nothing.
print(next(result))  # Checks 0 and yields 0.
print(next(result))  # Checks 1 and 2, then yields 2.
