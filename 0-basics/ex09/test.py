from ft_package import count_in_list

items = ["toto", "tata", "toto"]

assert count_in_list(items, "toto") == 2
assert count_in_list(items, "tutu") == 0
assert count_in_list([], "toto") == 0

print("All checks passed.")

