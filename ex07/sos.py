import sys


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        NESTED_MORSE = {
            "A": ".- ",
            "B": "-... ",
            "C": "-.-. ",
            "D": "-.. ",
            "E": ". ",
            "F": "..-. ",
            "G": "--. ",
            "H": ".... ",
            "I": ".. ",
            "J": ".--- ",
            "K": "-.- ",
            "L": ".-.. ",
            "M": "-- ",
            "N": "-. ",
            "O": "--- ",
            "P": ".--. ",
            "Q": "--.- ",
            "R": ".-. ",
            "S": "... ",
            "T": "- ",
            "U": "..- ",
            "V": "...- ",
            "W": ".-- ",
            "X": "-..- ",
            "Y": "-.-- ",
            "Z": "--.. ",
            "1": ".---- ",
            "2": "..--- ",
            "3": "...-- ",
            "4": "....- ",
            "5": "..... ",
            "6": "-.... ",
            "7": "--... ",
            "8": "---.. ",
            "9": "----. ",
            "0": "----- ",
            " ": "/ "
        }
        code = ""
        text = sys.argv[1]
        for i in text.upper():
            if i in NESTED_MORSE:
                code += NESTED_MORSE[i]
            else:
                raise AssertionError("the arguments are bad")
        code.strip()
        print(code)
    except AssertionError as e:
        print(f"AssertionError: {e}")


# your tests and your error handling
if __name__ == "__main__":
    main()
