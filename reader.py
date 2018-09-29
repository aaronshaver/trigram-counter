import fileinput
import sys


def read():
    lines = []

    try:
        with fileinput.input(openhook=fileinput.hook_encoded("utf-8")) as f:
            for line in f:
                lines.append(line.strip('\n'))
    except FileNotFoundError as e:
        print("Sorry, one of your paths could not be found. Please fix and try again.")
        print("Error details:\n" + str(e))
        sys.exit()

    return lines
