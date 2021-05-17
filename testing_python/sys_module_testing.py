"""Playing with the sys module"""

import sys
import math
import statistics

# sys.stderr.write("This is stderr text\n")
# sys.stderr.flush()
# sys.stdout.write("This is stdout text\n")

def summary(filename):
    """
    Reads a file and returns the sum, mean and stdev after the calculations.
    :param filename: str
    :return: int tuple
    """
    with open(filename, "r") as f:
        l = f.read().splitlines()
    values = [eval(i) for i in l if not i.isalpha()]
    summa = sum(values)
    mean = statistics.mean(values)
    std_dev = statistics.stdev(values)

    return (summa, mean, std_dev)

def main():
    """Takes all the arguments from commandline and calls the summary-function.
    Then prints the returned values."""

    for arg in sys.argv[1:]:
        s = summary(arg)
        print(f"File: {arg} Sum: {s[0]:.6f} Average: {s[1]:.6f} Stddev: {s[2]:.6f}")


if __name__ == "__main__":
    main()