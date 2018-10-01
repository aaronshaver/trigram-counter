# trigram-counter

This script counts three-word phrases (trigrams) across STDIN or multiple text files, and then displays the top 100 phrases to the console.

## Requirements

Please install Python 3.x. I tested the script successfully with Python 3.7.0 on Windows 10 and Python 3.5.2 on Ubuntu Linux.

## Usage

### Run the tests

    python -m unittest discover

### Get input from STDIN

    cat file.txt | python counter.py

### Get input from files

    python counter.py file1.txt file2.txt
    
## Design decisions and known limitations

Natural language processing can get complicated and I made some simplifying assumptions, such as:

1. Words like "Python's" will render as "python" "s" (two words).

2. It's up for debate whether you call this a bug or not, but I found that on Windows on Git Bash and in the default
commandline, the final entry for the command `python counter.py text/Origin.txt` will always be `33 - at the present`.
But in an Ubuntu VM, it was not deterministic. The last entry would float around among several phrases that scored 33.
You could "fix" this by doing a second sort on the dictionary such that whenever multiple phrases have the same score,
they get sorted in some kind of order like alphabetic. But this would be sort of arbitrary.
