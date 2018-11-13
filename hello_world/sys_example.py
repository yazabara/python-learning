import sys

__version__ = '0.1'


def print_console_arguments():
    for arg in sys.argv:
        print arg


def print_path_variable():
    print sys.path


if __name__ == '__main__':
    print_console_arguments()
    print_path_variable()
    # print all identifiers from sys
    print dir(sys)
