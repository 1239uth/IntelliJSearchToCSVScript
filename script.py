import sys  # for argv


def verify_argv():
    """
    Verify only 1 command line argument is passed and exit if there isn't.

    :return: None
    """
    input_format = f'Input Format: `python {__file__} <filename>`'
    if len(sys.argv) != 2:
        print(input_format)
        exit(1)


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    verify_argv()
    print_hi('Uthman')
