import sys


def main():
    """
    Print words whose length exceeds the supplied limit.

    Read the text and length limit from the command line and print the
    matching words as a list.
    """

    try:
        assert len(sys.argv) == 3
        assert sys.argv[2].isdigit()
    except AssertionError as error:
        print(f"{type(error).__name__}: the arguments are bad")
        print("Usage: filterstring.py [text] [lenght]")
        exit()

    text = sys.argv[1]
    lenght = int(sys.argv[2])
    words = text.split(' ')
    result = [word for word in words if (lambda w: len(w) > lenght)(word)]
    print(result)
    # words = [word for word in text.split(' ')]
    # has_lenght = filter(lambda word: len(word) > lenght, words)
    # print(list(has_lenght))


if __name__ == "__main__":
    main()
