import fileinput


def read():
    lines = []

    # TODO: just append to a string so we don't have to convert back and forth
    with fileinput.input() as f:
        for line in f:
            lines.append(line.strip('\n'))

    return lines
