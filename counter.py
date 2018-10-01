import multiprocessing
import re
from datetime import datetime

import reader
from counter_config import GRAM_SIZE, SEPARATOR, TOP_N_PHRASES

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


def find_grams(text, out_list):
    ## do work
    pass


def count(text):
    # 2% performance improvement; see notes.txt
    local_separator = SEPARATOR
    local_gram_size = GRAM_SIZE

    processes = 2  # number of processes to use to count the grams

    text_lists = []
    first_half_index = len(text) // 2  # TODO: fix hardcoded two sub-text divisions
    text_lists.append(text[:first_half_index])
    text_lists.append(text[first_half_index:])

    print()
    print(text_lists[0])
    print(text_lists[1])
    print()

    jobs = []
    for i in range(processes):
        out_list = list()
        process = multiprocessing.Process(target=find_grams, args=(text_lists[i], out_list))
        jobs.append(process)

    output = {}

    # pre-processing like lowercasing everything, removing non-alphanum chars
    text = local_separator.join(text)
    text = text.lower()
    stripped_text = re.sub(r'[^a-z0-9 ]+', local_separator, text)
    split_text = stripped_text.split()

    if len(split_text) < local_gram_size:
        return output
    else:
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
        f.write(timing_data + '\n')
        # caveat from reading SO: datetime.now() may have limited resolution,
        # be off by several ms so this isn't perfect
