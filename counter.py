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

    final_output = ', '.join(output_list)

    print(final_output)


def sort_counts(counts):
    # sort by highest count first
    return sorted(counts.items(), key=lambda key_value_pair: key_value_pair[1], reverse=True)


def main():
    input_data = reader.read()
    counts = count(input_data)
    print_counts(counts)


def count(text):
    output = {}

    text = SEPARATOR.join(text)
    text = text.lower()
    stripped_text = re.sub(r'[^a-z0-9 ]+', SEPARATOR, text)
    split_text = stripped_text.split()

    if len(split_text) < GRAM_SIZE:
        return output
    else:
        for i in range(len(split_text)):
            current_phrase = split_text[i:i + GRAM_SIZE]
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

    timing_data = str(datetime.now() - startTime)
    with open('performance.txt', 'a') as f:
        f.write(timing_data + '\n')
        # caveat from reading SO: datetime.now() may have limited resolution,
        # be off by several ms so this isn't perfect
