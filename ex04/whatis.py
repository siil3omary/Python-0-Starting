import sys

try:
    assert len(sys.argv) <= 2, "more than one argument is provided"
    if len(sys.argv) == 1:
        exit()
    if len(sys.argv) == 2:
        try:
            num = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")

    if num % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")

except AssertionError as e:
    print(f"AssertionError: {e}")
