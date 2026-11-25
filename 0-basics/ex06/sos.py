import sys


def main():
    """
    Print the Morse code for a command-line argument.

    Encode letters and digits and represent each input space with a slash.
    """

    try:
        assert len(sys.argv) == 2, "wrong number of arguments"
    except AssertionError as error:
        print(f"{type(error).__name__}: {error}")
        print("Usage: sos.py [text]")
        exit()

    text = sys.argv[1]
    morse_code = {
        "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
        "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
        "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
        "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
        "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
        "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
        "Y": "-.--",  "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.",
        " ": "/",
    }

    output = ""
    for char in text:
        try:
            assert char.upper() in morse_code, "the arguments are bad"
        except AssertionError as error:
            print(f"{type(error).__name__}: {error}")
            exit()
        morse = morse_code[char.upper()]
        output += morse + " "
    print(output)


if __name__ == "__main__":
    main()
