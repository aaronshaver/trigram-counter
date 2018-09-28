import re
from counter_config import GRAM_SIZE, SEPARATOR


def print_counts(counts):
    sorted_counts = sort_counts(counts)

    output_list = []
    for key, value in sorted_counts:
        next_count = '{0} - {1}'.format(value, key)
        output_list.append(next_count)

    final_output = ', '.join(output_list)

    print(final_output)


def sort_counts(counts):
    # sort by highest count first
    return sorted(counts.items(), key=lambda key_value_pair: key_value_pair[1], reverse=True)


def main():
    # TODO: fix bug where some weird 2 word phrases are showing!!!!
    # TODO: fix bug where some weird 2 word phrases are showing!!!!
    # TODO: fix bug where some weird 2 word phrases are showing!!!!
    # TODO: fix bug where some weird 2 word phrases are showing!!!!
    counts = count(["Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.[27] In July 2018, Van Rossum stepped down as the leader in the language community after 30 years.[28][29] Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.[30] Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software[31] and has a community-based development model, as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software Foundation."])
    print_counts(counts)


def count(texts):
    output = {}
    text = texts[0]
    text = text.lower()
    stripped_text = re.sub(r'[^a-z0-9 ]+', SEPARATOR, text)
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
