import sys


def str_filter(av):
    try:
        sh_len = int(av[2])
    except ValueError:
        raise AssertionError("the arguments are bad")
    words = av[1].split()
    # print(words)
    print([i for i in words if len(i) >= sh_len])


def main(ac, av):
    if ac == 3:
        str_filter(av)
    else:
        raise AssertionError("the arguments are bad")


if __name__ == "__main__":
    try:
        main(len(sys.argv), sys.argv)
    except AssertionError as e:
        print(f"AssertionError: {e}")
