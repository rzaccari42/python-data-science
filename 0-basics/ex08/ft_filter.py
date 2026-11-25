def ft_filter(function, iterable):
    (
        "Return an iterator yielding those items of iterable for which "
        "function(item)\n"
        "is true. If function is None, return the items that are true."
    )

    for item in iterable:
        if function is None:
            if item:
                yield item
        elif function(item):
            yield item


def main():
    """
    Serve as the script entry point.

    The script exits without producing output.
    """


if __name__ == "__main__":
    main()
