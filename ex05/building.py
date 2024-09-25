import sys


def count_digit(text: str):
    return sum(1 for char in text if char.isdigit())


def count_upper(text: str):
    return sum(1 for char in text if char.isupper())


def count_lower(text: str):
    return sum(1 for char in text if char.islower())


def count_ponct(text: str):
    count = 0
    for i in range(0, len(text)):
        if text[i] in ('!', ",", "\'", ";", "\"", ".", "-", "?"):
            count = count + 1
    return count


def count_space(text: str):
    count = 0
    for i in range(0, len(text)):
        if text[i] == " ":
            count += 1
    return count


def print_msg(text: str):
    lenght_of_text = len(text)
    len_upper = count_upper(text)
    len_lower = count_lower(text)
    len_ponct = count_ponct(text)
    len_space = count_space(text)
    len_digit = count_digit(text)
    print(f"The text contains {lenght_of_text} characters:")
    print(f"{len_upper} upper letters")
    print(f"{len_lower} lower letters")
    print(f"{len_ponct} punctuation marks")
    print(f"{len_space} spaces")
    print(f"{len_digit} digits")


def main():
    args = sys.argv
    lenArgs = len(args)
    try:
        if lenArgs > 2:
            raise AssertionError("more than one argument is provided")
        elif lenArgs == 2:
            text = args[1]
        elif lenArgs == 1:
            print("What is the text to count?")
            text = input("")
        print_msg(text)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
