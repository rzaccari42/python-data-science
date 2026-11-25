import sys

def check_odd_or_even(nbr):
    if nbr % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

try:
    assert len(sys.argv) <= 2, "more than one argument is provided"
    if len(sys.argv) == 1:
        exit()
    try:
        nbr = int(sys.argv[1])
        check_odd_or_even(nbr)
    except ValueError:
        raise AssertionError("argument is not an integer")
except AssertionError as error:
    print(f"{type(error).__name__}: {error}")
