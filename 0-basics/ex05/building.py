import sys


def main():
    """
    Print character counts for the supplied text.

    Read a command-line argument or prompt for standard input. Report
    the total and the counts of uppercase letters, lowercase letters,
    punctuation marks, whitespace characters, and digits.
    """

    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 1:
            print("What is the text to count?")
            text = sys.stdin.readline()
        else:
            text = sys.argv[1]
    except AssertionError as error:
        print(f"{type(error).__name__}: {error}")
        exit()
    except KeyboardInterrupt:
        exit()

    upper = lower = punct = space = digit = 0
    punct_symbols = ".,!?;:"
    for char in text:
        if char.isupper():
            upper += 1
        if char.islower():
            lower += 1
        if char in punct_symbols:
            punct += 1
        if char.isspace():
            space += 1
        if char.isdigit():
            digit += 1
    char_count = len(text)

    print(f"\nThe text contains {char_count} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits\n")


if __name__ == "__main__":
    main()
