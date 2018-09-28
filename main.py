GRAM_SIZE = 3  # for future if customer wants more or less than 3 word phrases
SPACE_CHAR = ' '


def main():
    # TODO: print output to console
    pass


def count(texts):
    output = {}
    if len(texts[0].split()) < GRAM_SIZE:
        return output
    else:
        texts_split = texts[0].split()

        for i in range(len(texts_split)):
            current_phrase = texts_split[i:i + GRAM_SIZE]
            if len(current_phrase) < GRAM_SIZE:
                break  # avoid testing tail end of text if < gram size

            joined_phrase = SPACE_CHAR.join(current_phrase)
            if joined_phrase not in output:
                output[joined_phrase] = 1
            else:
                output[joined_phrase] += 1
    return output


if __name__ == "__main__":
    main()
