import re
from counter_config import GRAM_SIZE, SEPARATOR, TOP_N_PHRASES
import reader
from datetime import datetime

startTime = datetime.now()


def print_counts(counts):
    sorted_counts = sort_counts(counts)

    output_list = []
    i = 0
    for key, value in sorted_counts:
        if i < TOP_N_PHRASES:
            next_count = '{0} - {1}'.format(value, key)
            output_list.append(next_count)
            i += 1
        else:
            break  # no need to waste cycles if we've already done top 100/etc.

    final_output = ', '.join(output_list)
    print(final_output)  # TODO: thinking 10/4 should return str for pure func


def sort_counts(counts):
    # sort by highest count first
    return sorted(counts.items(), key=lambda key_value_pair: key_value_pair[1],
                  reverse=True)


def count(text):
    output = {}

    # pre-processing like lowercasing everything, removing non-alphanum chars
    text = SEPARATOR.join(text)
    text = text.lower()
    stripped_text = re.sub(r'[^a-z0-9 ]+', SEPARATOR, text)
    split_text = stripped_text.split()

    if len(split_text) < GRAM_SIZE:  # avoid very small texts (< ngram size)
        return output
    else:
        # 2% performance improvement; see notes.txt
        local_separator = SEPARATOR
        local_gram_size = GRAM_SIZE
        for i in range(len(split_text)):
            # moves a three-word (by default) "window" across the text
            current_phrase = split_text[i:i + local_gram_size]
            if len(current_phrase) < local_gram_size:
                break  # avoid testing tail end of text if tail < gram size

            joined_phrase = local_separator.join(current_phrase)
            if joined_phrase in output:
                output[joined_phrase] += 1
            else:
                output[joined_phrase] = 1
    return output


def main():
    input_data = reader.read()
    counts = count(input_data)
    print_counts(counts)


if __name__ == "__main__":
    main()

    timing_data = str(datetime.now() - startTime)
    with open('performance.txt', 'a') as f:
        # TODO: ideally would convert to milliseconds for easier parsing later
        f.write(timing_data + '\n')
        # caveat from reading SO: datetime.now() may have limited resolution,
        # be off by several ms so this isn't perfect
