

import sys


def main():
    """
    Here you would put the spript that uses comand line arguments:
    """
    argument = sys.argv[0]
    print("The argument is: ", argument)


if __name__ == "__main__":
    main()


## Then, standing on the script folder, to time the stript do this in python comand line:
# > import timeit
# > from timeit_with_script import main
# > sys.argv[0] = 10 # emulate your arguments
# > timeit.timeit(main, number=100) # run the benchmark