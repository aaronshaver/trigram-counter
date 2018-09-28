import re
from counter_config import GRAM_SIZE, SEPARATOR


def main():
    # TODO: print output to console
    pass


def count(texts):
    output = {}
    text = texts[0]
    text = text.lower()
    stripped_text = re.sub(r'[^a-z ]+', SEPARATOR, text)
    text_split = stripped_text.split(SEPARATOR)

    if len(text_split) < GRAM_SIZE:
        return output
    else:
        for i in range(len(text_split)):
            current_phrase = text_split[i:i + GRAM_SIZE]
            if len(current_phrase) < GRAM_SIZE:
                break  # avoid testing tail end of text if tail < gram size

            joined_phrase = SEPARATOR.join(current_phrase)
            if joined_phrase not in output:
                output[joined_phrase] = 1
            else:
                output[joined_phrase] += 1
    return output


if __name__ == "__main__":
    main()
