"""Opens files with command line command and file adressess
shoul be provided in parameters as a string"""

import sys

def file_count(filename):
    """
    Counts lines, words and chars in the file and returns a tuple.
    :param filename: str
    :return: int (tuple)
    """
    line_count = 0
    word_count = 0
    char_count = 0
    with open(filename, "r") as file:
        for line in file:
            line_count += 1
            char_count += len(line)
            splitted = line.split(" ")
            for word in splitted:
                word = word.strip("\n")
                if word:
                    word_count += 1

    return (line_count, word_count, char_count)

def main():
    """Calls the file_count -function with arguments and prints returning values."""
    for arg in sys.argv[1:]:
        s = file_count(arg)
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{arg}")


if __name__ == "__main__":
    main()
