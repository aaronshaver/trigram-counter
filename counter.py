import re
from datetime import datetime
from multiprocessing import Process, Queue

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


def count_grams(split_text, collector_queue):
    # 2% performance improvement; see notes.txt
    local_separator = SEPARATOR
    local_gram_size = GRAM_SIZE

    counts = {}
    for i in range(len(split_text)):
        # moves a three-word (by default) "window" across the text
        current_phrase = split_text[i:i + local_gram_size]
        if len(current_phrase) < local_gram_size:
            break  # avoid testing tail end of text if tail < gram size

        joined_phrase = local_separator.join(current_phrase)
        if joined_phrase in counts:
            counts[joined_phrase] += 1
        else:
            counts[joined_phrase] = 1

    collector_queue.put(counts)


def process_text(text):

    # pre-processing like lowercasing everything, replacing non-alphanum chars
    text = SEPARATOR.join(text)
    text = text.lower()
    stripped_text = re.sub(r'[^a-z0-9 ]+', SEPARATOR, text)
    split_text = stripped_text.split()

    if len(split_text) < GRAM_SIZE:
        return {}  # got input so small that we couldn't even find ngrams in it
    else:
        processes = 2  # number of processes to use to count the ngrams
        collector_queue = Queue()

        text_lists = []
        first_half_index = len(split_text) // 2  # TODO: fix hardcoded two
        text_lists.append(split_text[:first_half_index])
        text_lists.append(split_text[first_half_index:])

        jobs = []
        for i in range(processes):
            # We split up the processing of the text into chunks for speed.
            # The args are the particular sub-section of the text plus an
            # accumulator as well as the local vars to avoid global var
            # slowdown.
            process = Process(target=count_grams, args=(text_lists[i],
                                                        collector_queue))
            jobs.append(process)

        combined_output = []
        for j in jobs:
            j.start()

        for j in jobs:
            combined_output.append(collector_queue.get())
            j.join()  # forces sync on all jobs being completed

    output = {}
    for d in combined_output:
        if output == {}:
            output = d.copy()
        else:
            # So this may be slow and may defeat the whole point of this
            # multiprocessing speed up; however, I didn't find a better
            # way of merging dictionaries than this invented one...
            #
            # Update: yep, it's pretty slow. Here's 4 times with and 4 times
            # without merging the dictionaries:
            # 0:00:01.605927
            # 0:00:01.612612
            # 0:00:01.650152
            # 0:00:01.614200
            # 0:00:01.511553
            # 0:00:01.518491
            # 0:00:01.498542
            # 0:00:01.495551
            #
            # The last 4 times are faster than any pre-multiprocessing times
            # I was getting, the best of those of which were around 1567 ms
            # But with the dict merge, things slow down to end up being
            # worse overall
            for key, value in d.items():
                if key in output:
                    output[key] = output[key] + value  # add to existing val
                else:
                    output[key] = value

    return output


def main():
    input_data = reader.read()
    counts = process_text(input_data)
    print_counts(counts)


if __name__ == "__main__":
    main()

    timing_data = str(datetime.now() - startTime)
    with open('performance.txt', 'a') as f:
        f.write(timing_data + '\n')
        # caveat from reading SO: datetime.now() may have limited resolution,
        # be off by several ms so this isn't perfect
